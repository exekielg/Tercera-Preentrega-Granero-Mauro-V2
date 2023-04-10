from django.http import HttpResponse
from django.contrib.auth import authenticate

def carrito(request):
    carrito = request.session.get('carrito', [])
    return {'carrito': carrito}







def importe_total_carro(request):
    total=0
    #if request.user.is_authenticated:
     #   for item in request.session["carrito"]:
     #       total= total+(float(item["precio"]))
    return {"importe_total_carro":total}

