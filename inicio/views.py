from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import Pelicula
from inicio.forms import PeliculaFormularioCrear, EditarPeliculaFormulario, PeliculaBusquedaFormulario
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy



def inicio(request):
    return render(request, r"inicio/inicio.html")

def agregar_pelicula(request):
    if request.method == "POST":
        formulario = PeliculaFormularioCrear(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            pelicula = Pelicula(titulo=data.get("titulo"), director =data["director"], sinopsis = data["sinopsis"])
            pelicula.save()
            return redirect("listado_peliculas")
        else:
            return render(request, r"inicio/agregar_pelicula.html", {"formulario": formulario})
    
    formulario = PeliculaFormularioCrear()
    return render(request, r"inicio/agregar_pelicula.html", {"formulario": formulario})

def listado_peliculas(request):
    formulario = PeliculaBusquedaFormulario(request.GET)
    if formulario.is_valid():
        titulo_a_buscar = formulario.cleaned_data.get("titulo")
        peliculas_encontradas = Pelicula.objects.filter(titulo__icontains= titulo_a_buscar)
    else:
        Pelicula.objects.all()
    
    formulario = PeliculaBusquedaFormulario()
    return render(request, r"inicio/listado_peliculas.html", {"formulario": formulario, "peliculas_encontradas": peliculas_encontradas})


def editar_pelicula(request, pelicula_id): 
    pelicula_a_editar = Pelicula.objects.get(id= pelicula_id)
    if request.method == "POST":
        formulario = EditarPeliculaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            pelicula_a_editar.titulo = data["titulo"]
            pelicula_a_editar.director = data["director"]
            pelicula_a_editar.sinopsis = data["sinopsis"]
            pelicula_a_editar.save()
            return redirect("listado_peliculas")
    formulario = EditarPeliculaFormulario(initial={"titulo": pelicula_a_editar.titulo, "director": pelicula_a_editar.director, "sinopsis": pelicula_a_editar.sinopsis})
    return render(request, r"inicio/editar_pelicula.html", {"formulario": formulario})


class PeliculaDeleteView(DeleteView):
    model = Pelicula
    template_name = "inicio/eliminar_pelicula.html"
    success_url = reverse_lazy("listado_peliculas")
    
class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "inicio/detalle_pelicula.html"
    