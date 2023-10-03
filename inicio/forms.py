from django import forms

class PeliculaFormulario(forms.Form):
    titulo = forms.CharField( max_length= 100)
    director = forms.CharField( max_length= 50)
    sinopsis = forms.CharField(widget= forms.Textarea)
    
class PeliculaBusquedaFormulario(forms.Form):
    titulo = forms.CharField( max_length= 100, required= False)
  
