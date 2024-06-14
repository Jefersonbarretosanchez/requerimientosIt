"""Modulo"""
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
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
            mensaje = render_to_string('requerimiento_creado.html', {
                'nombre_responsable': new_req.responsable,
                'nombre_requerimiento': new_req.requerimiento,
                'ticket_requerimiento': new_req.ticket,
                'alianza_solicitante': new_req.alianzasolicitante,
                'plataforma_relacionada': new_req.plataforma,
                'medio_carga': new_req.mediocarga,
                'area_solicitante': new_req.areasolicitante,
                'responsable_requerimiento': new_req.responsable,
                'fecha_creacion': new_req.fechacreacion,
                'usuario_nombre': request.user.first_name,
                'usuario_apellido': request.user.last_name,
            })
            para = [new_req.responsable.correo]
            de = "notificaciones.requerimientos@hotmail.com"

            email = EmailMultiAlternatives(
                asunto,
                mensaje,
                de,
                para
            )
            email.attach_alternative(mensaje, "text/html")
            email.send(fail_silently=False)
            
            # Correos adicionales para notificaciones
            control_requerimientos = [
                {"nombre": "Jeferson Barreto", "correo": "jefebasan97@gmail.com "},
                {"nombre": "Andres Vargas", "correo": "jefers97@gmail.com"},
            ]

            for referente in control_requerimientos:
                mensaje_referente = render_to_string('requerimiento_creado.html', {
                    'nombre_responsable': referente["nombre"],
                    'nombre_requerimiento': new_req.requerimiento,
                    'ticket_requerimiento': new_req.ticket,
                    'alianza_solicitante': new_req.alianzasolicitante,
                    'plataforma_relacionada': new_req.plataforma,
                    'medio_carga': new_req.mediocarga,
                    'area_solicitante': new_req.areasolicitante,
                    'responsable_requerimiento': new_req.responsable,
                    'fecha_creacion': new_req.fechacreacion,
                    'usuario_nombre': request.user.first_name,
                    'usuario_apellido': request.user.last_name,
                })
                para_referente = [referente["correo"]]

                email_referente = EmailMultiAlternatives(
                    asunto,
                    mensaje_referente,
                    de,
                    para_referente
                )
                email_referente.attach_alternative(mensaje_referente, "text/html")
                email_referente.send(fail_silently=False)

            return redirect('requerimientos')
        else:
            return self.form_invalid(form)


class RequerimientosUpdate(LoginRequiredMixin, UpdateView):
    """Actualiza Requerimientos"""
    model = Requerimientos
    form_class = RequerimientosFormEdit
    template_name = 'edit.html'
    success_url = reverse_lazy('requerimientos')

    def form_valid(self, form):
        response = super().form_valid(form)
        updated_req = self.object
        changed_fields = form.changed_data

        # Crear el contexto con los campos modificados
        cambios = {}
        for field in changed_fields:
            field_verbose_name = self.model._meta.get_field(field).verbose_name
            cambios[field_verbose_name] = form.cleaned_data[field]

        # Enviar correo electrónico con los campos modificados
        if cambios:
            asunto = "Requerimiento actualizado"
            mensaje_html = render_to_string('requerimiento_actualizado.html', {
                'nombre_responsable': updated_req.responsable,
                'nombre_requerimiento': updated_req.requerimiento,
                'cambios': cambios,
                'usuario_nombre': self.request.user.first_name,
                'usuario_apellido': self.request.user.last_name,
            })
            para = [updated_req.responsable.correo]
            de = "notificaciones.requerimientos@hotmail.com"

            email = EmailMultiAlternatives(
                asunto,
                mensaje_html,
                de,
                para
            )
            email.attach_alternative(mensaje_html, "text/html")
            email.send(fail_silently=False)

        # Correos adicionales para notificaciones de control
            control_requerimientos = [
                {"nombre": "Jeferson Barreto", "correo": "jeferson.barreto@scalalearning.com"},
                {"nombre": "Fabrizzio Garzon", "correo": "fabrizzio.garzon@scalalearning.com"},
            ]

            for referente in control_requerimientos:
                mensaje_html_referente = render_to_string('requerimiento_actualizado.html', {
                    'nombre_responsable': referente["nombre"],
                    'nombre_requerimiento': updated_req.requerimiento,
                    'cambios': cambios,
                    'usuario_nombre': self.request.user.first_name,
                    'usuario_apellido': self.request.user.last_name,
                })
                para_referente = [referente["correo"]]

                email_referente = EmailMultiAlternatives(
                    asunto,
                    mensaje_html_referente,
                    de,
                    para_referente
                )
                email_referente.attach_alternative(mensaje_html_referente, "text/html")
                email_referente.send(fail_silently=False)

        return HttpResponseRedirect(self.get_success_url() + '?updated=True')


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
