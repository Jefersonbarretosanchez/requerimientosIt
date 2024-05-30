"""Modulo"""
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, CreateView, UpdateView, FormView, TemplateView, DeleteView
from .forms import *
from tasks.models import Requerimientos


# Create your views here.
class Inicio(LoginRequiredMixin, TemplateView):
    """Funcion Lista Requerimientos En El Home"""
    template_name = 'dashboard.html'


class RequerimientosList(LoginRequiredMixin, ListView):
    """Función Lista Requerimientos En El Home"""
    model = Requerimientos
    template_name = 'requerimientos.html'
    context_object_name = 'requerimientos'
    paginate_by = 10

    def get_queryset(self):
        queryset = Requerimientos.objects.all().order_by('-fechacreacion')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(ticket__icontains=query) |
                Q(requerimiento__icontains=query) |
                Q(plataforma__plataforma__icontains=query) |
                Q(estado__estado__icontains=query) |
                Q(responsable__responsable__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        queryset = self.get_queryset()

        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            requerimientos = paginator.page(page)
        except PageNotAnInteger:
            requerimientos = paginator.page(1)
        except EmptyPage:
            requerimientos = paginator.page(paginator.num_pages)

        context['requerimientos'] = requerimientos
        context['page_obj'] = requerimientos
        context['is_paginated'] = requerimientos.has_other_pages()
        context['query'] = query

        return context


class RequerimientosCreate(LoginRequiredMixin, CreateView):
    """Creacion de Requerimientos"""
    model = Requerimientos
    template_name = 'create.html'
    form_class = RequerimientosForm
    success_url = reverse_lazy('requerimientos')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.user = request.user
            new_req.save()

            # Enviar correo electrónico al usuario que creó el requerimiento
            asunto = "Nuevo requerimiento creado"
            mensaje = """Se ha creado un nuevo requerimiento:

**ID:** {id_requerimiento}
**Nombre:** {nombre_requerimiento}
**Descripción:** {descripcion_requerimiento}
**Usuario Quien Lo Creo:** {nombre_usuario}

"""
            para = [new_req.user.email,'jeferson.barreto@scalalearning.com']  
            de = "notificaciones.requerimientos@hotmail.com"
            send_mail(
                asunto,
                mensaje.format(
                    id_requerimiento=new_req.id,
                    nombre_requerimiento=new_req.requerimiento,
                    descripcion_requerimiento=new_req.ticket,
                    nombre_usuario=new_req.user.username
                    # url_requerimiento=f"http://{request.get_host()}{reverse('requerimientos_detail', args=(new_req.id,))}"
                ),
                de,
                para,
                fail_silently=False
            )

            return redirect('requerimientos')


class RequerimientosUpdate(LoginRequiredMixin, UpdateView):
    """Actualiza Requerimientos"""
    model = Requerimientos
    form_class = RequerimientosFormEdit
    template_name = 'edit.html'
    success_url = reverse_lazy('requerimientos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RequerimientosDelete(LoginRequiredMixin, DeleteView):
    """Elimina Requerimientos"""
    model = Requerimientos
    template_name = 'requerimientos_confirm_delete.html'
    success_url = reverse_lazy('requerimientos')


class Login(FormView):
    model = User
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('requerimientos')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')


@login_required
def tablero(request):
    return render(request, 'tablero.html')
