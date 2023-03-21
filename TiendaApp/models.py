from django.db import models

# Create your models here.

# se crean los tipos de Productos que en este caso seran los tipos de Autos disponibles
class Categoria_Producto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'categoriaProd'
        verbose_name_plural = 'categoriasProd'

    def __str__(self):
        return self.nombre

# se Crean las Tablas con los productos (Autos disponibles)
class Producto(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    Categorias = models.ForeignKey(Categoria_Producto, on_delete= models.CASCADE)
    imagen = models.ImageField(upload_to= 'media', null=True, blank=True)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.marca + " " + self.modelo


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre, self.apellido
    


