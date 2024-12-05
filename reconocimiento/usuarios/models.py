from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    imagen_rostro = models.ImageField(upload_to='rostros/')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
