from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=200, help_text='Género o técnica empleada...')

    def __str__(self):
        return self.name


class trabajos(models.Model):

    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    year = models.DecimalField('Año', max_digits= 4, decimal_places=4)
    genero = models.ManyToManyField(Genero, help_text='Género o técnica empleada...')
    picture = models.FileField(upload_to='pictures', blank=True)
    fecha_publicado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['apellido', 'nombre']

    # def get_absolute_url(self):
    #     """Returns the url to access a particular author instance."""
    #     return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
