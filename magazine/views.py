from django.shortcuts import render, get_object_or_404
# Importamos los modelos
from .models import Article, Category
from django.core.paginator import Paginator

# Create your views here.


# * Vista magazine
def magazine(request):
    return render(request, 'magazine/magazine.html', {
        'titulo': 'Revista'
    }
    )


# *Vista de la lista de artículos
def list_articles(request):
    """
    Método que lista todos los artículos que existan creados
    de manera paginada
    """
    articles = Article.objects.all()
    # * Pagina los artículos
    paginar = Paginator(articles, 2)
    # * Recoger número de la página
    page = request.GET.get('page')
    article_page = paginar.get_page(page)
    return render(request, 'magazine/articles/list.html', {
        'title': 'Artículos',
        'articles': articles,
       # 'articles': article_page
    })


# * Vista de categorías
def categories(request, category_id):
    """
    Método para listar categorías dinámicamente
    """
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category_id)
    return render(request, 'magazine/categories/category.html', {
        'category': category
    })


def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'magazine/articles/detail.html', {
        'article': article
    })
