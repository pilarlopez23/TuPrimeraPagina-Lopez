from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import LogoutView, PasswordChangeView
from cuentas.forms import RegistroNuevoUsuario, EditarPerfil
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from cuentas.models import InfoExtra, User


def registro(request):
    if request.method == "POST":
        formulario = RegistroNuevoUsuario(request.POST, request.FILES)
        if formulario.is_valid():
            user = formulario.save()
           
            info_extra, created = InfoExtra.objects.get_or_create(user=user)
            if "avatar" in request.FILES:
                info_extra.avatar = request.FILES["avatar"] 
            if "pais" in request.POST:
                info_extra.pais = request.POST["pais"] 
            info_extra.save()
            user.save()
            return redirect("inicio")
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
            InfoExtra.objects.get_or_create(user=usuario)
            
            return redirect("inicio") 
    else:
        formulario = AuthenticationForm()
    
    return render(request, "cuentas/login.html", {"formulario": formulario})
        
@login_required
def editar_perfil(request):
    info_adicional = request.user.infoextra
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            if formulario.cleaned_data.get("avatar"):
                info_adicional.avatar = formulario.cleaned_data.get("avatar")
            if formulario.cleaned_data.get("pais"):
                info_adicional.pais = formulario.cleaned_data.get("pais")
            info_adicional.save()
            formulario.save()
            return redirect("detalle_perfil", pk=request.user.id) 
    else:
        formulario = EditarPerfil(initial={"avatar": info_adicional.avatar, "pais": info_adicional.pais}, instance= request.user)
    
    return render(request, "cuentas/editar_perfil.html", {"formulario": formulario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "cuentas/editar_pass.html"
    success_url = reverse_lazy("inicio")
    

class PerfilDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "cuentas/detalle_perfil.html"
    context_object_name ="usuario"

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       usuario = self.object 
       try:
        info_extra= InfoExtra.objects.get(user=usuario)
       except:
        info_extra = None 
       context["info_extra"] = info_extra
       return context
   