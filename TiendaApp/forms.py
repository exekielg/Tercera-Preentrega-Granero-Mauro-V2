from django import forms
from .models import Producto


# buscar producto en la BD
class ProductSearchForm(forms.Form):
    marca = forms.CharField(label='Marca', required=False)
    modelo = forms.CharField(label='Modelo', required=False)
    precio_min = forms.DecimalField(label='Precio Mínimo', decimal_places=2, required=False)
    precio_max= forms.DecimalField(label='Precio Máximo', decimal_places=2, required=False)

# agregar Cliente nuevo ala BD    
class ClienteForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    apellido = forms.CharField(label='Apellido', max_length=50)
    direccion = forms.CharField(label='Direccion',max_length=100)
    telefono = forms.CharField(label='Teléfono', max_length=20)
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    
    