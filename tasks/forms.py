from django import forms
from django.forms import ModelForm
from .models import Requerimientos


class RequerimientosForm(ModelForm):
    """Formulario para Registro de Requerimientos"""
    class Meta:
        """Modelo y campos"""
        model = Requerimientos
        fields = ['ticket', 'requerimiento',
                  'fechacreacion', 'mediocarga', 'plataforma', 'alianzasolicitante', 'areasolicitante', 'estado', 'responsable']
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

class RequerimientosFormEdit(ModelForm):
    """Formulario para Actualización de Requerimientos"""
    class Meta:
        """Modelo y campos"""
        model = Requerimientos
        fields = ['ticket', 'requerimiento',
                  'fechacreacion', 'fechapruebas', 'mediocarga', 'plataforma', 'alianzasolicitante', 'areasolicitante', 'estado', 'responsable','pasoproduccion','observaciones']
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
                    'id': 'id_requerimiento',
                    'disabled':True
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
                format='%Y-%m-%d',
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
            'pasoproduccion': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type':'date',
                    'class': 'form-control',
                    'placeholder': '',
                    'id': 'id_pasoproducción',
                }  
            ),
            'observaciones':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Introduzca las observacione en este campo',
                    'id':'id_observaciones'
                }
            )
        }
