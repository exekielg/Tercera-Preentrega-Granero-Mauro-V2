from django.shortcuts import render
from .carrito import Carrito
from TiendaApp.models import Producto
from django.shortcuts import redirect



def agregar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    if 'carrito' not in request.session:
        request.session['carrito'] = []
    carrito = request.session['carrito']
    carrito.append({
        'marca': producto.marca,
        'modelo': producto.modelo,
        'precio': producto.precio
    })
    request.session['carrito'] = carrito
    return redirect('Tienda')


def eliminar_prod(request, producto_id):
    carrito = request.session.get['carrito'], []  
    if producto_id in carrito:  
        del carrito[producto_id]  
        request.session['carito'] = carrito  
    return redirect('Tienda')  


def restar_producto(request,producto_id):
   carro=Carrito(request)
   producto=Producto.objects.get(id=producto_id)
   carro.restar_prod(producto=producto)   
   return redirect('tienda')    

def limpiar_carrito(request):
   carrito=Carrito(request)
   carrito.clear_carrito
   return render(request,'TiendaApp/tienda.html')   
