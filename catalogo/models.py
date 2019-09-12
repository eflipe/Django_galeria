from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=200, help_text='Género o técnica empleada...')

    def __str__(self):
        return self.nombre


class Pictures(models.Model):
    titulo = models.CharField(max_length=200, null=True, blank=True)
    pictures = models.FileField(upload_to='pictures', blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Pictures'
        ordering = ['-fecha_agregado']
        
    def __str__(self):
        return self.titulo


class Trabajos(models.Model):

    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    year = models.DecimalField('Año', max_digits= 4, decimal_places=0)
    genero = models.ManyToManyField(Genero, help_text='Género o técnica empleada...')
    pictures = models.ManyToManyField(Pictures, help_text='Cargar y seleccionar las imagenes...')
    fecha_publicado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Trabajos'
        ordering = ['-fecha_publicado']

    def __str__(self):
        return self.titulo


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
