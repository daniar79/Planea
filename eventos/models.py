from django.db import models


# Modulos para edición de fotos y texto.
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField

# Modulos para identificación de usuarios.
from django.contrib.auth.models import User
from django.utils.timezone import now

# Modulo par periodos de tiempo
from durationfield.forms import DurationField


# Create your models here.

# * Modelo para Tipos de eventos(Tipos)
class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(
        max_length=250, verbose_name="Descripción", null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    subtitle = models.CharField(
        max_length=255, verbose_name='Subtitulo', default='null', blank=True)
    ubication = RichTextField(default='Fuengirola',
                              verbose_name='Localización')
    content = RichTextField(verbose_name='Contenido')
    image = VersatileImageField(
        null=True, blank=True, verbose_name='Imagen', upload_to='events')
    public = models.BooleanField(default=False, verbose_name='Publicado')
    # ? Campo para identiicar a los usuarios de una tabla que existia Usuarios
    # ? editable quita el campo usuario visible
    user = models.ForeignKey(User, editable=False,
                             verbose_name="Autor", on_delete=models.CASCADE)
    # !OJO
    # ? Para relaciones de mucho a muchos se pone este campo  y se relaciona con related_name
    types = models.ManyToManyField(
        Type, verbose_name='Tipos', null=True, blank=True, related_name='eventos')
    begin = models.DateTimeField(
        verbose_name="Comienza", default=now)
    time_period = models.DurationField(
        editable=True, verbose_name='Durarión', default='Null')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    update_at = models.DateTimeField(
        auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-begin']

    def __str__(self) -> str:
        return self.title
