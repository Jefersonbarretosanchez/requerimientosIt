from django.contrib import admin
from .models import Requerimientos,MedioCarga,Plataforma,Estado,AlianzaSolicitante,AreaSolicitante,Responsable

class RequerimientosAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Requerimientos"""
    list_display=["id","ticket",'requerimiento','fechaCreacion','estado']
    readonly_fields=("fechaRegistro",'fechaActualizacion')
    search_fields=['ticket','requerimiento']
    list_filter = ['estado']
    ordering=['-fechaCreacion','requerimiento']
    list_display_links=['ticket']
    list_per_page=25 #Paginacion
    
class MedioCargaAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Medio Carga"""
    list_display=["id",'medioCarga']
    readonly_fields=("fechaRegistro",'fechaActualizacion')

class PlataformaAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Plataforma"""
    list_display=["id",'plataforma']
    readonly_fields=("fechaRegistro",'fechaActualizacion')
    
class EstadoAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Estado"""
    list_display=['id','estado']
    readonly_fields=("fechaRegistro",'fechaActualizacion')

class AlianzaAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Alianza"""
    list_display=["id",'alianzaSolicitante']
    readonly_fields=("fechaRegistro",'fechaActualizacion')
    
class AreaAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Areas"""
    list_display=["id",'areaSolicitante']
    readonly_fields=("fechaRegistro",'fechaActualizacion')
    
class ResponsableAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Responsables"""
    list_display=["id",'responsable']
    readonly_fields=("fechaRegistro",'fechaActualizacion')
# Register your models here.
admin.site.register(Requerimientos, RequerimientosAdmin)
admin.site.register(MedioCarga,MedioCargaAdmin)
admin.site.register(Plataforma,PlataformaAdmin)
admin.site.register(Estado,EstadoAdmin)
admin.site.register(AlianzaSolicitante,AlianzaAdmin)
admin.site.register(AreaSolicitante,AreaAdmin)
admin.site.register(Responsable,ResponsableAdmin)