from django.urls import path
from cuentas.views import login, LogoutView, registro, editar_perfil, CambiarContrasenia

urlpatterns = [
    path("login/", login, name= "login"),
    path("nuevo-registro/", registro , name= "registro"),
    path("perfil/editar/", editar_perfil , name= "editar_perfil"),
    path("perfil/editar/contraseña", CambiarContrasenia.as_view() , name= "editar_pass"),
    path("logout/", LogoutView.as_view(template_name="cuentas/logout.html"), name="logout"),
]
