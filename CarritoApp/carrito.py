
from TiendaApp.models import Producto

# Creacion de la clase Carrito de compras con la logica del mismo

class Carrito:
     def _init_(self, request):
        self.request=request
        self.session=request.session
        carrito=self.session.get("carrito")
        if not carrito:
            carrito=self.session["carrito"]= {}
        else:
            self.carrito=carrito

     def agregar(self, producto):
        if(str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio": str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+producto.precio
                    break
        self.guardar()

# Func para guardar el carro en la sesion        
     def guardar(self):
        self.session["carrito"]= self.carrito
        self.session.modified= True

# func p elimnar un  prod
     def eliminar(self,producto):
        producto.id= str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
        self.guardar()

# func p restar un  prod
     def restar_prod(self, producto):
        for key, value in self.carrito.items():
             if key==str(producto.id):
                value["cantidad"]= value["cantidad"]-1
                if value["cantidad"]< 1:
                     self.eliminar(producto)
                break
        self.guardar()
# func p Limpiar todo el carro
     def clear_carrito(self):
        self.session["carrito"]= {}
        self.session.modified= True