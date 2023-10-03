from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Pelicula
from inicio.forms import PeliculaFormulario, PeliculaBusquedaFormulario


def inicio(request):
    datos = {
        "fecha" : datetime.now()
    }
    
    return render(request, r"inicio/inicio.html", datos)

def agregar_pelicula(request):
    if request.method == "POST":
        formulario = PeliculaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            pelicula = Pelicula(titulo=data.get("titulo"), director =data["director"], sinopsis = data["sinopsis"])
            pelicula.save()
        else:
            return render(request, r"inicio/agregar_pelicula.html", {"formulario": formulario})
    
    formulario = PeliculaFormulario()
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
