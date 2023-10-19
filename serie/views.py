from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from serie.models import Serie
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class SerieCreateView(LoginRequiredMixin, CreateView):
    model = Serie
    fields = ["titulo", "creador", "sinopsis", "temporadas", "fecha_estreno"]  
    template_name= "serie/crear_serie.html"
    success_url = reverse_lazy("listado_series")

class SerieDeleteView(LoginRequiredMixin, DeleteView):
    model = Serie
    template_name = "serie/eliminar_serie.html"
    success_url = reverse_lazy("listado_series")

class SerieUpdateView(LoginRequiredMixin, UpdateView):
    model = Serie
    fields = ["titulo", "creador", "sinopsis", "temporadas", "fecha_estreno"]  
    template_name = "serie/editar_serie.html"
    success_url = reverse_lazy("listado_series")

class SerieDetailView(DetailView):
    model = Serie
    template_name = "serie/detalle_serie.html"

class SerieListView(ListView):
    model = Serie
    context_object_name = "listado_series"
    template_name = "serie/listado_series.html"
    
    def get_queryset(self):
        titulo_a_buscar = self.request.GET.get("titulo", None)
        if titulo_a_buscar:
            series = self.model.objects.filter(titulo__icontains=titulo_a_buscar)
        else:
            series = self.model.objects.all()
        return series




# Create your views here.
