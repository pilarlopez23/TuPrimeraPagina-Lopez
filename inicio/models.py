from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length= 100)
    director = models.CharField(max_length=50)
    sinopsis = models.TextField(default=" ")
    
    def __str__(self):
        return f"{self.titulo} {self.director} {self.sinopsis}"
