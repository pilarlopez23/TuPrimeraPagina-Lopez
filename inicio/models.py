from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length= 100)
    director = models.CharField(max_length=50)