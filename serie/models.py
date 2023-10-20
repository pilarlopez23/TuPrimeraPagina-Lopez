from django.db import models
from ckeditor.fields import RichTextField

class Serie(models.Model):
    titulo = models.CharField(max_length= 100)
    creador = models.CharField(max_length=50)
    sinopsis = RichTextField(default=" ")
    temporadas = models.IntegerField()
    fecha_estreno = models.DateField()
    portada = models.ImageField(null=True)
        
    def __str__(self):
        return f"{self.titulo} {self.creador} {self.sinopsis} {self.temporadas} {self.fecha_estreno} {self.portada}"