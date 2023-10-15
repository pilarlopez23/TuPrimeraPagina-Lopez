from django.urls import path
from cuentas.views import login

urlpatterns = [
    path("cuentas/", login, name= "login"),
]
