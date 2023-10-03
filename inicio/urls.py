from django.urls import path
from inicio.views import inicio, agregar_pelicula


urlpatterns = [
    path("", inicio, name= "inicio"),
  
    path("pelicula/agregar", agregar_pelicula, name= "agregar_pelicula")
]



  #path("agregar-pelicula/<str:titulo>/<str:director>/<str:sinopsis>", agregar_pelicula, name= "agregar_pelicula")