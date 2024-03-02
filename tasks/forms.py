from django.forms import ModelForm
from .models import Requerimientos


class RequerimientosForm(ModelForm):
    """Formnulario para Registro de Requerimientos"""
    class Meta:
        """Modelo y campos"""
        model=Requerimientos
        fields=['ticket', 'requerimiento','fechaCreacion','fechaPruebas']