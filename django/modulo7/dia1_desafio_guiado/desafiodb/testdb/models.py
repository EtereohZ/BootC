from django.db import models

# Create your models here.

class Chocolate(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=15)
    grado_ricura = models.IntegerField()