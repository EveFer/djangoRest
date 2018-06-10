from __future__ import unicode_literals

from django.db import models

# Create your models here. 
class Carrera(models.Model):
	nombre = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nombre

class User(models.Model):
	num_control = models.IntegerField()
	nombre = models.CharField(max_length=50)
	apellido_pat = models.CharField(max_length=50)
	apellido_mat = models.CharField(max_length=50)
	sexo = models.CharField(max_length=50)
	fecha_nac = models.DateField()
	direccion = models.TextField()
	carrera = models.ForeignKey(Carrera, verbose_name="diagnostico Carrera")
	
	def __str__(self):
		return self.nombre
