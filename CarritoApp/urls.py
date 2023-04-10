from django.urls import path
from CarritoApp import views

#app_name= 'carro'


urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('restar_prod/<int:producto_id>/',views.restar_producto, name= "restar"),
    path('clear_carrito/',views.limpiar_carrito, name= "limpiar"),

]





 
