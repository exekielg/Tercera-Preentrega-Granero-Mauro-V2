from django.urls import path
from TiendaApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name='Home'),
    path('clientes/',views.clientes, name='Clientes'),
    path('tienda/',views.tienda, name='Tienda'),
    path('contacto/',views.contacto, name='Contacto'),
    path('buscar_producto/',views.buscar_producto, name='Buscar'),
    path('resultados_busqueda/', views.buscar_producto, name='resultados_busqueda'),
   
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
