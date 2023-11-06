from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

  
class RegistroNuevoUsuario(UserCreationForm):
    username = forms.CharField(label= "Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    avatar = forms.ImageField(label="Foto de perfil", required=False)
    pais = forms.CharField(label="País") 
    
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "avatar","pais"]
        help_texts = {campo: " " for campo in fields}
        

class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label = "Cambiar email")
    first_name = forms.CharField(label = "Cambiar nombre", max_length= 25)
    last_name = forms.CharField(label="Cambiar Apellido", max_length=25)
    avatar = forms.ImageField(label="Foto de perfil", required=False)
    pais = forms.CharField(label="País") 
    
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "avatar", "pais"]
        

class CambiarContrasenia(PasswordChangeForm):
    password1 = forms.CharField(label="Nueva Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["password1", "password2"]
        help_texts = {campo: " " for campo in fields}