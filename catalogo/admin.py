from django.contrib import admin
from catalogo.models import Genero, Trabajos, Autor, Pictures

class TrabajosAdmin(admin.ModelAdmin):
    fields = ['autor', 'year', 'titulo', 'genero', 'pictures']
    list_display = ['titulo', 'autor', 'year']
    list_filter = ('autor', 'year')


admin.site.register(Genero)
admin.site.register(Trabajos, TrabajosAdmin)
admin.site.register(Autor)
admin.site.register(Pictures)
