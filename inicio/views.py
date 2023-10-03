from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Pelicula
from inicio.forms import PeliculaFormulario


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
