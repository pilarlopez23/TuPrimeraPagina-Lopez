from django.shortcuts import render
from django.urls import reverse_lazy
from serie.models import Serie
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class SerieCreateView(CreateView):
    model = Serie
    fields = ["titulo", "creador", "sinopsis", "temporadas", "fecha_estreno"]  
    template_name= "serie/crear_serie.html"
    success_url = reverse_lazy("series")

class SerieDeleteView(DeleteView):
    model = Serie
    template_name = "serie/eliminar_serie.html"
    success_url = reverse_lazy("series")

class SerieUpdateView(UpdateView):
    model = Serie
    fields = ["titulo", "creador", "sinopsis", "temporadas", "fecha_estreno"]  
    template_name = "serie/editar_serie.html"
    success_url = reverse_lazy("series")

class SerieDetailView(DetailView):
    model = Serie
    template_name = "serie/detalle_serie.html"

class SerieListView(ListView):
    model = Serie
    template_name = "serie/listado_series.html"



# Create your views here.
