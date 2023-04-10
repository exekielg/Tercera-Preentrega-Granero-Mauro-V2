from django.urls import path
from CarritoApp import views

#app_name= 'carro'


urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('elimina_prod/<int:producto_id>/', views.eliminar_prod, name='eliminar_prod'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar_producto'),   
    path('restar_prod/<int:producto_id>/',views.restar_producto, name= "restar"),
    #path('clear_carrito/',views.limpiar_carrito, name= "limpiar"),
    #path('limpiar-carrito/', views.limpiar_carrito, name='limpiar_carrito'),
    

]





 
