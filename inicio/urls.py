from django.urls import path
from inicio.views import inicio, agregar_pelicula, listado_peliculas, editar_pelicula
from inicio import views



urlpatterns = [
    path("", inicio, name= "inicio"),
    path("peliculas/", listado_peliculas, name= "listado_peliculas"),
    path("pelicula/agregar/", agregar_pelicula, name= "agregar_pelicula"),
    path("pelicula/<int:pelicula_id>/editar/", editar_pelicula, name= "editar_pelicula"),
    path("pelicula/<int:pk>/", views.PeliculaDetailView.as_view(), name= "detalle_pelicula"),
    path("pelicula/<int:pk>/eliminar/", views.PeliculaDeleteView.as_view() , name= "eliminar_pelicula"),
]



  #path("agregar-pelicula/<str:titulo>/<str:director>/<str:sinopsis>", agregar_pelicula, name= "agregar_pelicula")