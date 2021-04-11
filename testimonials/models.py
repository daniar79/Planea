from django.db import models


# Create your models here.
class Testimonial(models.Model):
    title = models.CharField(max_length=30, verbose_name='Título')
    content = models.CharField(max_length=150, verbose_name='Opinión')
    imagen = models.ImageField(
        default='null', verbose_name='Fotografía', upload_to='images')
    autor = models.CharField(max_length=40, verbose_name='Nombre del autor')
    profesion_localidad = models.CharField(
        max_length=50, verbose_name='Profesión - localidad')
    create_at = models.DateTimeField(verbose_name='Creado ', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Actualizado', auto_now=True)

    class Meta:
        verbose_name = 'Opinión'
        verbose_name_plural = 'Opiniones'

    def __str__(self) -> str:
        return self.title
