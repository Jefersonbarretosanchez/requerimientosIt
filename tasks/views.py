"""Modulo"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from .forms import *
from .models import Requerimientos, MedioCarga, AlianzaSolicitante, AreaSolicitante, Plataforma, Estado, Responsable
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView,CreateView,UpdateView
from django.core.paginator import Paginator

# Create your views here.


class Inicio(View):
    """Funcion Lista Requerimientos En El Home"""
    model = Requerimientos
    template_name = 'requerimientos.html'
    # context_object_name = 'requerimientos'
    # queryset = Requerimientos.objects.all().order_by('-fechacreacion')
    paginate_by = 10
    form_class=RequerimientosForm
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-fechacreacion')
    
    def get_context_data(self):
        contexto={}
        contexto['requerimiento']=self.get_queryset()
        contexto['form']=self.form_class
        return contexto
        
    def get(self,request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data())
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            new_req=form.save(commit=False)
            new_req.user = request.user
            print(new_req)
            new_req.save()
            return redirect('inicio')
    
class RequerimientosList(ListView):
    """Funcion Lista Requerimientos En El Home"""
    model = Requerimientos
    template_name = 'requerimientos.html'
    paginate_by = 10
    context_object_name = 'requerimientos'
    queryset = Requerimientos.objects.all().order_by('-fechacreacion')
    form_class=RequerimientosForm
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-fechacreacion')
    
    def get_context_data(self):
        contexto={}
        contexto['requerimientos']=self.get_queryset()
        contexto['form']=self.form_class
        return contexto
        
    def get(self,request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data())
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            new_req=form.save(commit=False)
            new_req.user = request.user
            print(new_req)
            new_req.save()
            return redirect('requerimientos')

class ActivosList(ListView):
    """Funcion Lista Requerimientos En El Home"""
    model = Activos
    template_name = 'home.html'
    paginate_by = 10
    form_class=ActivosForm
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-fechaingreso')
    
    def get_context_data(self):
        contexto={}
        contexto['activos']=self.get_queryset()
        contexto['form']=self.form_class
        return contexto
        
    def get(self,request,*args,**kwargs):
        return render(request, self.template_name,self.get_context_data())
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            new_req=form.save(commit=False)
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


@login_required
def signout(request):
    logout(request)
    return redirect('signin')


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
