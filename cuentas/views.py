from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import LogoutView, PasswordChangeView
from cuentas.forms import RegistroNuevoUsuario, EditarPerfil
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from cuentas.models import InfoAdicional

def registro(request):
    if request.method == "POST":
        formulario = RegistroNuevoUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect("login")
    else:
        formulario = RegistroNuevoUsuario()  
    
    return render(request, "cuentas/registro.html", {"formulario": formulario})


def login(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get("username")
            password = formulario.cleaned_data.get("password")
            usuario = authenticate(username=username, password=password)
            django_login(request, usuario)
            InfoAdicional.objects.get_or_create(user=usuario)
            
            return redirect("inicio") 
    else:
        formulario = AuthenticationForm()
    
    return render(request, "cuentas/login.html", {"formulario": formulario})
        
@login_required
def editar_perfil(request):
    info_adicional = request.user.infoadicional
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, request.FILES, instance= request.user)
        if formulario.is_valid():
            info_adicional.avatar= formulario.cleaned_data.get("avatar")
            info_adicional.save()
            formulario.save()
            return redirect("inicio")
    else:
        formulario = EditarPerfil(initial= {"avatar": info_adicional.avatar}, instance= request.user)
    
    return render(request, "cuentas/editar_perfil.html", {"formulario": formulario})
  
 
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "cuentas/editar_pass.html"
    success_url = reverse_lazy("editar_perfil.html")
