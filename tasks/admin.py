from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin
from .models import Requerimientos,MedioCarga,Plataforma,Estado,AlianzaSolicitante,AreaSolicitante,Responsable

# class RequerimientosResources(resources.ModelResource):
#     """Importar exportar"""
#     fields=(
#         'id',
#         'ticket',
#         'requerimiento',
#         'fechacreacion',
#         'sprintdesarrollo'
#         'fechapruebas',
#         'mediocarga',
#         'plataforma',
#     )
#     class Meta:
#         model=Requerimientos

class RequerimientosAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Requerimientos"""
    # resource_class=RequerimientosResources
    list_display=["ticket",'requerimiento','fechacreacion','plataforma','estado']
    readonly_fields=("fecharegistro",'fecha_actualizacion')
    search_fields=['ticket','requerimiento']
    list_filter = ['estado','plataforma']
    ordering=['-fechacreacion','requerimiento']
    #ordering=['-id']
    list_display_links=['ticket']
    list_per_page=25 #Paginacion
    
class MedioCargaAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Medio Carga"""
    list_display=['mediocarga']
    readonly_fields=("fechaRegistro",'fechaActualizacion')

class PlataformaAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Plataforma"""
    list_display=['plataforma']
    readonly_fields=("fechaRegistro",'fechaActualizacion')
    
class EstadoAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Estado"""
    list_display=['estado']
    readonly_fields=("fechaRegistro",'fechaActualizacion')

class AlianzaAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Alianza"""
    list_display=['alianzasolicitante']
    readonly_fields=("fechaRegistro",'fechaActualizacion')
    
class AreaAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Areas"""
    list_display=['areasolicitante']
    readonly_fields=("fechaRegistro",'fechaActualizacion')
    
class ResponsableAdmin(admin.ModelAdmin):
    """Configuracion Modulo Admin Responsables"""
    list_display=['responsable']
    readonly_fields=("fechaRegistro",'fechaActualizacion')
# Register your models here.
admin.site.register(Requerimientos, RequerimientosAdmin)
admin.site.register(MedioCarga,MedioCargaAdmin)
admin.site.register(Plataforma,PlataformaAdmin)
admin.site.register(Estado,EstadoAdmin)
admin.site.register(AlianzaSolicitante,AlianzaAdmin)
admin.site.register(AreaSolicitante,AreaAdmin)
admin.site.register(Responsable,ResponsableAdmin)