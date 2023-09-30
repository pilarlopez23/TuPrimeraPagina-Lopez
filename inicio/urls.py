from django.urls import path
from inicio.views import inicio, agregar_pelicula


urlpatterns = [
    path("", inicio),
    path("agregar-pelicula/<str:titulo>/<str:director>", agregar_pelicula)
]
