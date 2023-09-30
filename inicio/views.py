from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Pelicula


def inicio(request):
    datos = {
        "fecha" : datetime.now()
    }
    
    return render(request, r"inicio/inicio.html", datos)


def agregar_pelicula(request, titulo, director):
    pelicula = Pelicula(titulo=titulo, director=director)
    pelicula.save()
    
    
    return render(request, r"inicio/pelicula_agregada.html", {})

