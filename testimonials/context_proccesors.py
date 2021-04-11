from .models import Testimonial


# ? Función que genera testimonios dinámicos

def get_testimonials(request):
    # Añadimos el filter para visulaizar los visbles
    testimonials = Testimonial.objects.all().order_by('?')[:3]
    return{
        'testimonials': testimonials
    }
