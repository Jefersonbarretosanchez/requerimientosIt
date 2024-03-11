from django import forms
from django.forms import ModelForm
from .models import Requerimientos,Activos


class RequerimientosForm(ModelForm):
    """Formulario para Registro de Requerimientos"""
    class Meta:
        """Modelo y campos"""
        model = Requerimientos
        fields = ['ticket', 'requerimiento',
                  'fechacreacion', 'fechapruebas', 'mediocarga', 'plataforma', 'alianzasolicitante', 'areasolicitante', 'estado', 'responsable']
        widgets = {
            'ticket': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero Ticket',
                    'required': 'required',
                    'id': 'id_ticket'
                }
            ),
            'requerimiento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre Requerimiento',
                    'required': 'required',
                    'id': 'id_requerimiento'
                }
            ),
            'fechacreacion': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Fecha Creacion Req',
                    'required': 'required',
                    'id': 'id_fechaCreacion',
                }
            ),
            'fechapruebas': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Fecha Pruebas Req',
                    'id': 'id_fechaPruebas',
                }
            ),
            'mediocarga': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Medio Carga',
                    'required': 'required',
                    'id': 'id_medioCarga',
                }
            ),
            'plataforma': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Plataforma',
                    'required': 'required',
                    'id': 'id_plataforma',
                }
            ),
            'alianzasolicitante': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Alianza',
                    'required': 'required',
                    'id': 'id_alianzaSolicitante',
                }
            ),
            'areasolicitante': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Area',
                    'required': 'required',
                    'id': 'id_areaSolicitante',
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Estado',
                    'required': 'required',
                    'id': 'id_estado',
                }
            ),
            'responsable': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Responsable',
                    'required': 'required',
                    'id': 'id_responsable',
                }
            ),
        }

class ActivosForm(ModelForm):
    """Formulario para Registro de Requerimientos"""
    class Meta:
        """Modelo y campos"""
        model = Activos
        fields = ['identificacion', 'nombrecompleto',
                  'fechaingreso', 'estado', 'cargo', 'area', 'correo_electronico']
        widgets = {
            'identificacion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero identificacion',
                    'required': 'required',
                    'id': 'id_identificacion'
                }
            ),
            'nombrecompleto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre nombrecompleto',
                    'required': 'required',
                    'id': 'id_nombrecompleto'
                }
            ),
            'fechaingreso': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Fecha ingreso Req',
                    'required': 'required',
                    'id': 'id_fechaingreso',
                }
            ),
            'estado': forms.DateInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Estado',
                    'id': 'id_estado',
                }
            ),
            'cargo': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cargo',
                    'required': 'required',
                    'id': 'id_cargo',
                }
            ),
            'area': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'area',
                    'required': 'required',
                    'id': 'id_area',
                }
            ),
            'correo_electronico': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Correo',
                    'required': 'required',
                    'id': 'id_correo_electronico',
                }
            )
        }
