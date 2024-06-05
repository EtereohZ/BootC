from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    tarea_id = models.ForeignKey('Tarea', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    