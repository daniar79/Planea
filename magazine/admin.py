from django.contrib import admin

# Register your models here.
from .models import Category, Article
# ? Creamos la clase categorias administrativas para mostrar información modo lectura


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']  # Ojo se arregla poniendo corchetes
    search_fields = ('name', 'description')
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    ordering = ['name']


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at', 'user')
    search_fields = ('title', 'subtitle', 'user__username', 'categories__name','published')
    list_display = ('title', 'user', 'public', 'published')
    list_filter = ('title', 'public', 'created_at', 'user__username')
    date_hierarchy='published'
    list_filter = ('user__username', 'categories__name')

    def post_categories(self,obj):
        return "," .join ([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description="Categorías"
        

    def save_model(self, request, obj, form, change):
        """
        Creamos la función que devuelve el usuario grabado auto
        usa los parametros: self, obj, request,form,change (self siempre primero)
        """
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()


# ? Configuración personalizada del panel y pasamos los modelos creados
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
