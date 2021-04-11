from django.db import models
from django.db.models.base import Model

# Create your models here.


class guia(models.Model):
    title = models.CharField(max_length=50, verbose_name='Título')
    subtitle = models.CharField(max_length=80, verbose_name='Subtítulo')
    tipo = models.CharField(max_length=20, verbose_name='Tipo')
    ubicacion=models.CharField(max_length=200,verbose_name='Ubicación')
