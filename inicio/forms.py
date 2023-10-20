from django import forms
from ckeditor.fields import RichTextFormField

class PeliculaFormularioBase(forms.Form):
    titulo = forms.CharField( max_length= 100)
    director = forms.CharField( max_length= 50)
    sinopsis = RichTextFormField()
    portada = forms.ImageField(required=False)
    
class PeliculaFormularioCrear(PeliculaFormularioBase):
    pass

class EditarPeliculaFormulario(PeliculaFormularioBase):
    pass 

class PeliculaBusquedaFormulario(forms.Form):
    titulo = forms.CharField( max_length= 100, required= False)
  
