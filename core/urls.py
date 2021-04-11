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
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings

urlpatterns = [
    # Paths del core
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("contact/", views.contact, name='contact'),


    path("covid-19/", views.covid_19, name='covid-19'),
    path("events/", views.events, name='events'),
    path("guies-routes/", views.guies_routes, name='guies_routes'),
    path("weather/", views.weather, name='weather'),
    path("social-media/", views.social_media, name='social_media'),
    path("legal-information/", views.legal_info, name='legal_infoemation'),

]

# Configuración para la carga de imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
