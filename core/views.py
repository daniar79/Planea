from django.shortcuts import render, HttpResponse


# Create your views here.

# * Vista home
def home(request):
    return render(request, 'core/index.html', {
        'titulo': 'Inicio'
    }
    )


# * Vista about
def about(request):
    return render(request, 'core/about.html', {
        'titulo': 'About'
    }
    )


# * Vista guias y rutas
def guies_routes(request):
    return HttpResponse(
        """<h1>Guías y Rutas</h1>
        <p>Lista de servicios</p>
        """
    )


# * Vista eventos
def events(request):
    return HttpResponse(
        """<h1>Eventos</h1>
        <p>Lista de eventos</p>
        """
    )


# * Vista services
def services(request):
    return HttpResponse(
        """<h1>Servicios</h1>
        <p>Lista de servicios</p>
        """
    )


# * Vista services
def covid_19(request):
    return HttpResponse(
        """<h1>Medidas</h1>
        <p>Medidas actuales</p>
        """
    )


# * Vista el tiempo
def weather(request):
    return HttpResponse(
        """<h1>El tiempo</h1>
        <p>El tiempo en Fuengirola</p>
        """
    )


# * Vista de contacto
def contact(request):
    return HttpResponse(
        """<h1>Contacto</h1>
        <p>Formulario</p>
        """
    )


# * Vista de aviso legal
def legal_info(request):
    return HttpResponse(
        """<h1>Aviso legal</h1>
        <p>Información legal</p>
        """
    )


# * Vista redes sociales
def social_media(request):
    return HttpResponse(
        """<h1>Servicios</h1>
        <p>Lista de servicios</p>
        """
    )
