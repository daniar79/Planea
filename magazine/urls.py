"""Planea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Paths del core
    path("magazine/", views.magazine, name='magazine'),
    # * lista todos los articulos
    path('magazine/articulos/', views.list_articles, name='lista articulos'),
    # * Lista los aritculos por categorias
    path('magazine/categoria/<int:category_id>',
         views.categories, name='categorias'),
    path('magazine/articulo/<int:article_id>', views.article, name='articulo'),
]
