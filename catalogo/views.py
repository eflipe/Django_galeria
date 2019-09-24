from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from catalogo.models import Autores, Pictures, Genero
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PicturesListView(generic.ListView):
    model = Pictures
    context_object_name = 'pictures'
    queryset = Pictures.objects.all().order_by('-fecha_agregado')
    template_name = 'catalogo/index.html'
    paginate_by = 8



# def index(request):
#     trabajos = Autores.objects.all()
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
    model = Autores
    context_object_name = 'trabajos'
    template_name = 'catalogo/autores_info.html'


class AutoresDetailView(generic.DetailView):
    model = Autores
    context_object_name = 'autor_detalle'
    template_name = 'catalogo/autores_detalle.html'


class PicturesDetailView(generic.DetailView):
    model = Pictures
    context_object_name = 'pictures_detalle'
    template_name = 'catalogo/pictures_detalle.html'


class TrabajosCreate(CreateView):
    model = Autores
    fields = '__all__'
    success_url = reverse_lazy('index')


class TrabajosUpdate(UpdateView):
    model = Autores
    fields = '__all__'


class TrabajosDelete(DeleteView):
    model = Autores
    success_url = reverse_lazy('autores')


class PicturesCreate(CreateView):
    model = Pictures
    fields = '__all__'

    def get_initial(self):
        return {'autor': self.object.autor.id}

    def get_initial(self):
        autor = get_object_or_404(Pictures, pk=self.kwargs.get('pk'))
        return {
            'autor': autor,
        }

    def get_success_url(self):
        return reverse_lazy('autores-detalle', kwargs={'pk': self.kwargs['pk']})



class AutorCreate(CreateView):
    model = Autores
    fields = '__all__'
    success_url = reverse_lazy('autores')


class GeneroCreate(CreateView):
    model = Genero
    fields = '__all__'
    success_url = reverse_lazy('autor_create')
