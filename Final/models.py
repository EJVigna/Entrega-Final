from django.db import models

# Create your models here.

class Zapatos (models.Model):
    tipo = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    numero = models.IntegerField()
    
class Cliente (models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    condicion = models.CharField(max_length=20)

class Proveedor (models.Model):
    razonsocial = models.CharField(max_length=40)
    condicion = models.CharField(max_length=20)
    mail = models.EmailField()