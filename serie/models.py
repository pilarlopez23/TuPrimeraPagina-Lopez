from django.db import models

class Serie(models.Model):
    titulo = models.CharField(max_length= 100)
    creador = models.CharField(max_length=50)
    sinopsis = models.TextField()
    temporadas = models.IntegerField()
    fecha_estreno = models.DateField()
    
    def __str__(self):
        return f"{self.titulo} {self.creador}"