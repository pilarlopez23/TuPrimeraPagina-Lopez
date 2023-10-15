from django.db import models
from ckeditor.fields import RichTextField

class Pelicula(models.Model):
    titulo = models.CharField(max_length= 100)
    director = models.CharField(max_length=50)
    sinopsis = RichTextField()
    
    def __str__(self):
        return f"{self.titulo} {self.director} {self.sinopsis}"
