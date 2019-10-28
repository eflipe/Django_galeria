from django.urls import path
from . import views

urlpatterns = [
    path('', views.PicturesListView.as_view(), name='index'),
    path('autores/', views.AutoresListView.as_view(), name='autores'),
    path('autores/<int:pk>', views.AutoresDetailView.as_view(), name='autores-detalle'),
    path('pictures/<int:pk>', views.PicturesDetailView.as_view(), name='pictures-detalle'),
    path('autor/create/', views.AutorCreate.as_view(), name='autor_create'),
    path('genero/create/', views.GeneroCreate.as_view(), name='genero_create'),
    path('pictures/<int:pk>/create/', views.PicturesCreate.as_view(), name='pictures_create'),


]
