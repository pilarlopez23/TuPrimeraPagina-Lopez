from django.urls import path
from inicio.views import inicio, agregar_pelicula, listado_peliculas


urlpatterns = [
    path("", inicio, name= "inicio"),
    path("pelicula", listado_peliculas, name= "peliculas"),
    path("pelicula/agregar", agregar_pelicula, name= "agregar_pelicula")
]



  #path("agregar-pelicula/<str:titulo>/<str:director>/<str:sinopsis>", agregar_pelicula, name= "agregar_pelicula")