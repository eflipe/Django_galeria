from django.urls import path
from . import views

urlpatterns = [
    path('', views.PicturesListView.as_view(), name='index'),
    path('autores/', views.AutoresListView.as_view(), name='autores'),
    path('autores/<int:pk>', views.AutoresDetailView.as_view(), name='autores-detalle'),
    path('pictures/<int:pk>', views.PicturesDetailView.as_view(), name='pictures-detalle'),
    path('autores/create/', views.TrabajosCreate.as_view(), name='author_create'),
    path('autor/create/', views.AutorCreate.as_view(), name='autor_create'),
    path('genero/create/', views.GeneroCreate.as_view(), name='genero_create'),
    path('pictures/<int:pk>/create/', views.PicturesCreate.as_view(), name='pictures_create'),
    path('autores/<int:pk>/update/', views.TrabajosUpdate.as_view(), name='author_update'),
    path('autores/<int:pk>/delete/', views.TrabajosDelete.as_view(), name='author_delete'),


]
