from django.contrib import admin
from catalogo.models import Genero, Autores, Pictures

class AutoresAdmin(admin.ModelAdmin):
    fields = ['nombre', 'apellido', 'website', 'genero', 'bio']
    list_display = ['apellido', 'nombre', 'website']
    list_filter = ('apellido',)


admin.site.register(Genero)
admin.site.register(Autores, AutoresAdmin)
# admin.site.register(Autor)
admin.site.register(Pictures)
