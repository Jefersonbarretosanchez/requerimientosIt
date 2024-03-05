"""Modulo"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import RequerimientosForm
from .models import Requerimientos, MedioCarga, AlianzaSolicitante, AreaSolicitante, Plataforma, Estado, Responsable
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    reqs = Requerimientos.objects.all()
   # cuando se quiera mostrar losm datos del usuario Logeado reqs = Requerimientos.objects.filter(user=request.user)
    if request.method == 'GET':
        return render(request, 'requerimientos.html', {'reqs': reqs})
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
