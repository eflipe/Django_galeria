from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.models import Trabajos, Pictures
from django.views import generic


class PicturesListView(generic.ListView):
    model = Pictures
    context_object_name = 'pictures'
    queryset = Pictures.objects.all().order_by('-fecha_agregado')
    template_name = 'catalogo/index.html'
    paginate_by = 8



# def index(request):
#     trabajos = Trabajos.objects.all()
#     pictures = Pictures.objects.all().order_by('-fecha_agregado')
#     context = {
#         'trabajos': trabajos,
#         'pictures': pictures
#     }
#
#     template = 'catalogo/index.html'
#
#     return render(request, template, context=context)


class AutoresListView(generic.ListView):
    model = Trabajos
    context_object_name = 'trabajos'
    template_name = 'catalogo/autores_info.html'


class AutoresDetailView(generic.DetailView):
    model = Trabajos
    context_object_name = 'autor_detalle'
    template_name = 'catalogo/autores_detalle.html'


class PicturesDetailView(generic.DetailView):
    model = Pictures
    context_object_name = 'pictures_detalle'
    template_name = 'catalogo/pictures_detalle.html'
