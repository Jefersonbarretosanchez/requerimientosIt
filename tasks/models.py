"""Importa modelos"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Requerimientos(models.Model):
    """Class representing a requerimiento"""
    ticket=models.CharField(max_length=100)
    requerimiento=models.CharField(max_length=100, blank=True)
    fechaCreacion=models.DateField(blank=False)
    fechaPruebas=models.DateField(null=True)
    fechaRegistro=models.DateTimeField(auto_now_add=True)
    fechaActualizacion=models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.requerimiento) + str(self.ticket)
    #+ ' by ' + str(self.user.username)