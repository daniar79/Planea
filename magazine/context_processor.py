from magazine.models import Category, Article
from django.db.models import Count


# ? Función que genera categorias de forma dinámicas

def get_categories(request):
    """
    métodod que obtiene todas las categorías creadas.
    También flitramos por los articulos creados y publicados,
    para no tener que mostrar todos las categorias vacias.

    Sacamos la lista por la categoriy_id y en texto plano
    filtra las categorias que tienen ids -->filter(id__in=ids
    """
    ids_in_use = Article.objects.filter(
        public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(
        id__in=ids_in_use).values_list('id', 'name')
    return{
        'categories': categories,
        'ids': ids_in_use
    }

def prueba(request):
 
    return  'prueba'
