from django import forms
from django.forms import ModelForm
from .models import Requerimientos


class RequerimientosForm(ModelForm):
    """Formulario para Registro de Requerimientos"""
    class Meta:
        """Modelo y campos"""
        model = Requerimientos
        fields = ['ticket', 'requerimiento',
                  'fechaCreacion', 'fechaPruebas', 'medioCarga', 'plataforma', 'alianzaSolicitante', 'areaSolicitante', 'estado', 'responsable']
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
            'fechaCreacion': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Fecha Creacion Req',
                    'required': 'required',
                    'id': 'id_fechaCreacion',
                }
            ),
            'fechaPruebas': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Fecha Pruebas Req',
                    'id': 'id_fechaPruebas',
                }
            ),
            'medioCarga': forms.Select(
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
            'alianzaSolicitante': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Alianza',
                    'required': 'required',
                    'id': 'id_alianzaSolicitante',
                }
            ),
            'areaSolicitante': forms.Select(
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
