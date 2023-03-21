from django import forms
from .models import Producto


# buscar producto en la BD por MARCA de Auto
class BusquedaForm(forms.Form):
    marca = forms.CharField(label='Marca', max_length=50)

# agregar Cliente nuevo ala BD    
class ClienteForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    apellido = forms.CharField(label='Apellido', max_length=50)
    direccion = forms.CharField(label='Direccion',max_length=100)
    telefono = forms.CharField(label='Teléfono', max_length=20)
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    
    