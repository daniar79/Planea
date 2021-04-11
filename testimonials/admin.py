from django.contrib import admin
from .models import Testimonial


# Register your models here.

# Configuración de Admin Testimonial
class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('title', 'content')
    list_display = ('title', 'autor', 'create_at')
    ordering = ('-create_at',)


# Configuración personalizada del panel.
admin.site.register(Testimonial, TestimonialAdmin)

title = "Proyecto Planea"
subtitle = "Panel de Gestión "
