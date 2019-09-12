from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.models import Trabajos, Pictures

# index: ordenar por fecha de agregado.


def index(request):
    trabajos = Trabajos.objects.all()
    pictures = Pictures.objects.all().order_by('-fecha_agregado')
    context = {
        'trabajos': trabajos,
        'pictures': pictures
    }

    template = 'catalogo/index.html'

    return render(request, template, context=context)
