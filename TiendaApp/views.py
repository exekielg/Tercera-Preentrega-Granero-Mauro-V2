from django.shortcuts import render, redirect
from .models import Categoria_Producto, Producto, Cliente
from .forms import BusquedaForm, ClienteForm

# Register your models here.

# Create your models here.



def home(request):
    return render(request, 'TiendaApp/home.html')

def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo cliente en la base de datos
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            direccion =form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, direccion=direccion,telefono=telefono,email=email)
            nuevo_cliente.save()
            return render(request, 'TiendaApp/clientes.html', {'form': form, 'mensaje':'OK'})
    else:
        form = ClienteForm()
    return render(request, 'TiendaApp/clientes.html', {'form': form})





def tienda(request):
    producto = Producto.objects.all()
    return render(request, 'TiendaApp/tienda.html', {"Productos": producto})

def contacto(request):
        return render(request, 'TiendaApp/contacto.html')


# buscar producto Auto, por marca
def buscar_producto(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            productos = Producto.objects.filter(marca__icontains=marca)
            return render(request, 'TiendaApp/resultados_busqueda.html', {'productos': productos})
    else:
        form = BusquedaForm()
    return render(request, 'TiendaApp/buscar_producto.html', {'form': form})