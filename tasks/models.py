"""Importa modelos"""
from django.db import models
from django.contrib.auth.models import User
from .choices import sprints

# Create your models here.
class MedioCarga(models.Model):
    """Class representa los medios de carga"""
    medioCarga=models.CharField(max_length=50)
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.medioCarga)
       
class Plataforma(models.Model):
    """Class representa las plataformas"""
    plataforma=models.CharField(max_length=50)
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.plataforma)

class Estado(models.Model):
    """Class representa los estados"""
    estado=models.CharField(max_length=50)
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.estado)

class AlianzaSolicitante(models.Model):
    """Class representa las alianzas"""
    alianzaSolicitante=models.CharField(max_length=50)
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.alianzaSolicitante)

class AreaSolicitante(models.Model):
    """Class representa las Areas"""
    areaSolicitante=models.CharField(max_length=50)
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.areaSolicitante)

class Responsable(models.Model):
    """Class representa los responsables"""
    responsable=models.CharField(max_length=50)
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.responsable)

class Requerimientos(models.Model):
    """Class representing a requerimiento"""
    ticket=models.CharField(max_length=100,verbose_name="# Ticket")
    requerimiento=models.CharField(max_length=100, blank=True, verbose_name="Nombre Requerimiento")
    fechaCreacion=models.DateField(blank=False, verbose_name="Fecha Creación")
    sprintDesarrollo=models.CharField(max_length=100,choices=sprints, default='Sin Sprint', verbose_name="Sprint Desarrollo")
    fechaPruebas=models.DateField(null=True,blank=True,verbose_name="Fecha Pruebas")
    medioCarga=models.ForeignKey(MedioCarga,null=True,blank=True,on_delete=models.PROTECT, verbose_name="Medio De Carga")
    plataforma=models.ForeignKey(Plataforma,null=True,blank=True,on_delete=models.PROTECT, verbose_name="Plataforma")
    estado=models.ForeignKey(Estado,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Estado De Ejecución")
    alianzaSolicitante=models.ForeignKey(AlianzaSolicitante,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Alianza")
    areaSolicitante=models.ForeignKey(AreaSolicitante,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Area")
    responsable=models.ForeignKey(Responsable,null=True,blank=True,on_delete=models.PROTECT,verbose_name="Responsable")
    pasoProduccion=models.DateField(null=True, blank=True,verbose_name="Fecha Paso Producción")
    observaciones=models.TextField(null=True,blank=True,verbose_name="Observaciones y/o Avances")
    fechaRegistro=models.DateTimeField(auto_now_add=True,verbose_name="Fecha Registro BD")
    fechaActualizacion=models.DateTimeField(auto_now=True,verbose_name="Fecha Actualización BD")
    user= models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Usuario")
        
    def __str__(self):
        return str(self.requerimiento)
    #+ ' by ' + str(self.user.username)
