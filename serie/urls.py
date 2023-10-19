from django.urls import path
from serie import views

urlpatterns = [
    path("series/", views.SerieListView.as_view(), name= "listado_series"),
    path("series/crear", views.SerieCreateView.as_view(), name= "crear_serie"),
    path("series/<int:pk>/eliminar/", views.SerieDeleteView.as_view(), name= "eliminar_serie"),
    path("series/<int:pk>/editar/", views.SerieUpdateView.as_view(), name= "editar_serie"),
    path("series/<int:pk>/", views.SerieDetailView.as_view(), name= "detalle_serie"),
]
