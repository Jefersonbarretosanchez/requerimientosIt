from django.contrib import admin
from .models import Requerimientos

class RequerimientosAdmin(admin.ModelAdmin):
    """Ver campos de solo lectura"""
    readonly_fields=("fechaRegistro",)
# Register your models here.
admin.site.register(Requerimientos, RequerimientosAdmin)
