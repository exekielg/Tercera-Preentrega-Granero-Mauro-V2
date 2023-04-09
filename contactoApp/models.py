from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'