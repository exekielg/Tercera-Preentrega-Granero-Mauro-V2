from django.shortcuts import render
from .carrito import Carrito
from TiendaApp.models import Producto
from django.shortcuts import redirect


def agregar_producto(request,producto_id):
   carro=Carrito(request)
   producto=Producto.objects.get(id=producto_id)
   carro.agregar(producto=producto)   #agregar del carrito.py
   return redirect('Tienda')      #redirigir a Tienda

def eliminar_producto(request,producto_id):
   carro=Carrito(request)
   producto=Producto.objects.get(id=producto_id)
   carro.eliminar(producto=producto)    # func del carrito.py
   return redirect('Tienda')    #redirigir a Tienda

def restar_producto(request,producto_id):
   carro=Carrito(request)
   producto=Producto.objects.get(id=producto_id)
   carro.restar_prod(producto=producto)    # func del carrito.py
   return redirect('Tienda')    #redirigir a Tienda

def limpiar_carrito(request,producto_id):
   carro=Carrito(request)
   carro.clear_carrito
   return redirect('Tienda')    #redirigir a Tienda
