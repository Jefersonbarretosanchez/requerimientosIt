"""Modulo"""
import datetime
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View, ListView, CreateView, UpdateView, FormView, TemplateView,DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tasks.forms import *
from tasks.models import Requerimientos, MedioCarga, AlianzaSolicitante, AreaSolicitante, Plataforma, Estado, Responsable


# Create your views here.


class Inicio(LoginRequiredMixin, TemplateView):
    """Funcion Lista Requerimientos En El Home"""
    template_name = 'dashboard.html'

class RequerimientosList(LoginRequiredMixin, ListView):
    """Funcion Lista Requerimientos En El Home"""
    model = Requerimientos
    template_name = 'requerimientos.html'
    context_object_name = 'requerimientos'
    queryset = Requerimientos.objects.all().order_by('-fechacreacion')
    paginate_by = 10
    
    # def get_queryset(self):
    #     query=self.request.GET.get('search')
    #     post_list=Requerimientos.objects.filter(
    #         Q(ticket=query) | Q(requerimiento=query)
    #     ).distinct()
    #     return post_list
        
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
            print(new_req)
            new_req.save()
            return redirect('requerimientos')

class RequerimientosUpdate(LoginRequiredMixin,UpdateView):
    """Actualiza Requerimientos"""
    model = Requerimientos
    form_class = RequerimientosFormEdit
    template_name = 'edit.html'
    success_url = reverse_lazy('requerimientos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RequerimientosDelete(LoginRequiredMixin,DeleteView):
    """Elimina Requerimientos"""
    model=Requerimientos
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
    
class ActivosList(LoginRequiredMixin, ListView):
    """Funcion Lista Requerimientos En El Home"""
    model = Activos
    template_name = 'home.html'
    paginate_by = 10
    form_class = ActivosForm

    def get_queryset(self):
        return self.model.objects.all().order_by('-fechaingreso')

    def get_context_data(self):
        contexto = {}
        contexto['activos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.user = request.user
            print(new_req)
            new_req.save()
            return redirect('activos')


@login_required
def home(request):
   # cuando se quiera mostrar losm datos del usuario Logeado reqs = Requerimientos.objects.filter(user=request.user)
    if request.method == 'GET':
        return render(request, 'requerimientos.html', {'reqs': reqs, "page_obj": page_obj})
    else:
        try:
            form = RequerimientosForm(request.POST)
            new_req = form.save(commit=False)
            new_req.user = request.user
            new_req.save()
            return redirect('requerimientos')
        except ValueError:
            return render(request, 'requerimientos.html', {
                'reqs': reqs,
                'form': RequerimientosForm,
                'error': 'Ingresa datos validos'
            })


def signup(request):
    if request.method == 'GET':
        print('Metodo GET')
        return render(request, 'login.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registra usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
            except IntegrityError:
                return render(request, 'login.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'login.html', {
            'form': UserCreationForm,
            'error': 'Contraseñas No Coinciden :('
        })


@login_required
def requerimientos(request):
    reqs = Requerimientos.objects.all()
    medios = MedioCarga.objects.all()
    plataformas = Plataforma.objects.all()
    estados = Estado.objects.all()
    alianzas = AlianzaSolicitante.objects.all()
    areas = AreaSolicitante.objects.all()
    responsables = Responsable.objects.all()
    paginate_by = 10
   # cuando se quiera mostrar losm datos del usuario Logeado reqs = Requerimientos.objects.filter(user=request.user)
    if request.method == 'GET':
        return render(request, 'requerimientos.html', {
            'reqs': reqs,
            'medios': medios,
            'plataformas': plataformas,
            'estados': estados,
            'alianzas': alianzas,
            'areas': areas,
            'responsables': responsables,
            'form': RequerimientosForm
        })
    else:
        try:
            form = RequerimientosForm(request.POST)
            new_req = form.save(commit=False)
            new_req.user = request.user
            new_req.save()
            return redirect('requerimientos')
        except ValueError:
            return render(request, 'requerimientos.html', {
                'reqs': reqs,
                'medios': medios,
                'plataformas': plataformas,
                'estados': estados,
                'alianzas': alianzas,
                'areas': areas,
                'responsables': responsables,
                'form': RequerimientosForm,
                'error': 'Ingresa datos validos'
            })

@login_required
def create_req(request):
    if request.method == 'GET':
        return render(request, 'home.html', {
            'form': RequerimientosForm
        })
    else:
        try:
            form = RequerimientosForm(request.POST)
            new_req = form.save(commit=False)
            new_req.user = request.user
            new_req.save()
            return redirect('requerimientosc')
        except ValueError:
            return render(request, 'home.html', {
                'form': RequerimientosForm,
                'error': 'Ingresa datos validos'
            })

@login_required
def req_detail(request, reql_id):
    reql = get_object_or_404(Requerimientos, pk=reql_id)
    return render(request, 'req_detail.html', {'reql': reql})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario No valido'
            })
        else:
            login(request, user)
            return redirect('requerimientos')

@login_required
def tablero(request):
    return render(request, 'tablero.html')
