from django.db import models
# Modulos para edición de fotos y texto.
from ckeditor.fields import RichTextField
from versatileimagefield.fields import VersatileImageField
# Modulos para identificación de usuarios.
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.


# * Modelo para Categorías
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(
        max_length=250, verbose_name="Descripción", null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    subtitle = models.CharField(
        max_length=255, verbose_name='Subtitulo', default='null', blank=True)
    lead = RichTextField(default='null', verbose_name='Entrada')
    content = RichTextField(verbose_name='Contenido')
    image = VersatileImageField(
        null=True, blank=True, verbose_name='Imagen', upload_to='articles')
    public = models.BooleanField(default=False, verbose_name='Publicado')
    # ? Campo para identiicar a los usuarios de una tabla que existia Usuarios
    # ? editable quita el campo usuario visible
    user = models.ForeignKey(User, editable=False,
                             verbose_name="Autor", on_delete=models.CASCADE)
    # !OJO
    # ? Para relaciones de mucho a muchos se pone este campo  y se relaciona con related_name
    categories = models.ManyToManyField(
        Category, verbose_name='Categorías', null=True, blank=True, related_name='articulos')
    published=models.DateTimeField(verbose_name="Fecha de publicación",default=now)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    update_at = models.DateTimeField(
        auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'
        ordering=['-published']

    def __str__(self) -> str:
        return self.title
