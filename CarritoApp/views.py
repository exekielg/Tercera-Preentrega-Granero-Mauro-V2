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


def ver_carrito(request):
    carrito = request.session.get('carrito', [])
    total = sum([p['precio'] for p in carrito])
    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})




'''def agregar_producto(request,producto_id):
   carro=Carrito(request)
   producto=Producto.objects.get(id=producto_id)
   carro.agregar(producto=producto)   #agregar del carrito.py
   return redirect('Tienda')      #redirigir a Tienda'''

'''def eliminar_producto(request,producto_id):
   carro=Carrito(request)
   producto=Producto.objects.get(id=producto_id)
   carro.eliminar(producto=producto)    # func del carrito.py
   return redirect('Tienda')    #redirigir a Tienda '''

def eliminar_producto(request, producto_id):
    if 'carrito' in request.session:
        carrito = request.session['carrito']
        for item in carrito:
            if item['id'] == producto_id:
                carrito.remove(item)
        request.session['carrito'] = carrito
    return redirect('carrito')


def restar_producto(request,producto_id):
   carro=Carrito(request)
   producto=Producto.objects.get(id=producto_id)
   carro.restar_prod(producto=producto)    # func del carrito.py
   return redirect('Tienda')    #redirigir a Tienda

def limpiar_carrito(request,producto_id):
   carro=Carrito(request)
   carro.clear_carrito
   return redirect('Tienda')    #redirigir a Tienda
