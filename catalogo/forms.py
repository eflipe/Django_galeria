from django.forms import ModelForm
from catalog.models import Trabajos


class TrabajosModelForm(ModelForm):
    class Meta:
        model = Trabajos
        exclude = ['fecha_publicado']
