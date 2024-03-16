"""Importa modelos"""
from django.db import models
from django.contrib.auth.models import User
from .choices import sprints

# Create your models here.
class MedioCarga(models.Model):
    """Class representa los medios de carga"""
    mediocarga=models.CharField(max_length=50,verbose_name="Medio De Carga")
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.mediocarga)
       
class Plataforma(models.Model):
    """Class representa las plataformas"""
    plataforma=models.CharField(max_length=50,verbose_name="Plataforma")
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.plataforma)

class Estado(models.Model):
    """Class representa los estados"""
    estado=models.CharField(max_length=50,verbose_name="Estado")
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.estado)

class AlianzaSolicitante(models.Model):
    """Class representa las alianzas"""
    alianzasolicitante=models.CharField(max_length=50,verbose_name="Alianza")
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.alianzasolicitante)

class AreaSolicitante(models.Model):
    """Class representa las Areas"""
    areasolicitante=models.CharField(max_length=50,verbose_name="Area")
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.areasolicitante)

class Responsable(models.Model):
    """Class representa los responsables"""
    responsable=models.CharField(max_length=50,verbose_name="Responsable")
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.responsable)

class Requerimientos(models.Model):
    """Class representing a requerimiento"""
    ticket=models.CharField(max_length=100,verbose_name="# Ticket")
    requerimiento=models.CharField(max_length=100, blank=True, verbose_name="Nombre Requerimiento")
    fechacreacion=models.DateField(blank=False, verbose_name="Fecha Creación")
    sprintdesarrollo=models.CharField(max_length=100,choices=sprints, default='Sin Sprint', verbose_name="Sprint Desarrollo")
    fechapruebas=models.DateField(null=True,blank=True,verbose_name="Fecha Pruebas")
    mediocarga=models.ForeignKey(MedioCarga,null=True,blank=True,on_delete=models.PROTECT, verbose_name="Medio De Carga")
    plataforma=models.ForeignKey(Plataforma,null=True,blank=True,on_delete=models.PROTECT, verbose_name="Plataforma")
    estado=models.ForeignKey(Estado,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Estado De Ejecución")
    alianzasolicitante=models.ForeignKey(AlianzaSolicitante,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Alianza")
    areasolicitante=models.ForeignKey(AreaSolicitante,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Area")
    responsable=models.ForeignKey(Responsable,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Responsable")
    pasoproduccion=models.DateField(null=True, blank=True,verbose_name="Fecha Paso Producción")
    observaciones=models.TextField(null=True,blank=True,verbose_name="Observaciones y/o Avances")
    fecharegistro=models.DateTimeField(auto_now_add=True,verbose_name="Fecha Registro BD")
    fecha_actualizacion=models.DateTimeField(auto_now=True,verbose_name="Fecha Actualización BD")
    user= models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Usuario")
    
    class Meta:
        verbose_name_plural='Requerimientos'
        verbose_name='Requerimiento'
        db_table  = "requerimientos"
        
    def __str__(self):
        return str(self.requerimiento)
    #+ ' by ' + str(self.user.username)

class Activos(models.Model):
    """Class representing a requerimiento"""
    identificacion=models.CharField(max_length=100,verbose_name="# Identificacion")
    nombrecompleto=models.CharField(max_length=100, blank=True, verbose_name="Nombre Completo")
    fechaingreso=models.DateField(blank=False, verbose_name="Fecha Ingreso")
    estado=models.CharField(max_length=100, verbose_name="Estado")
    cargo=models.CharField(max_length=100,verbose_name="Cargo")
    area=models.CharField(max_length=100,verbose_name="Area")
    correo_electronico=models.EmailField(verbose_name="Correo")
    #estado=models.ForeignKey(Estado,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Estado De Ejecución")
    # alianzasolicitante=models.ForeignKey(AlianzaSolicitante,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Alianza")
    # areasolicitante=models.ForeignKey(AreaSolicitante,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Area")
    # responsable=models.ForeignKey(Responsable,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Responsable")
    # pasoproduccion=models.DateField(null=True, blank=True,verbose_name="Fecha Paso Producción")
    # observaciones=models.TextField(null=True,blank=True,verbose_name="Observaciones y/o Avances")
    # fecharegistro=models.DateTimeField(auto_now_add=True,verbose_name="Fecha Registro BD")
    # fecha_actualizacion=models.DateTimeField(auto_now=True,verbose_name="Fecha Actualización BD")
    user= models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Usuario")
        
    def __str__(self):
        return str(self.nombrecompleto)
    #+ ' by ' + str(self.user.username)

class Pruebas(models.Model):
    """Prueba"""
    nombre = models.CharField(blank=True, max_length=50)
    
    class Meta:
        verbose_name_plural="Prueba T"
        verbose_name="Prueba"