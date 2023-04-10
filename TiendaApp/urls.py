from django.urls import path, include
from django.contrib import admin
from TiendaApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home, name='Home'),
    path('clientes/',views.clientes, name='Clientes'),
    path('tienda/',views.tienda, name='Tienda'),
    path('buscar_producto/',views.buscar_producto, name='Buscar'),
    path('resultados_busqueda/', views.buscar_producto, name='resultados_busqueda'),
    path('login', views.login_request, name = 'Login'),
    path ('register', views.register, name = 'Register'),
    path('logout/', views.logout_view, name='Logout'),


    
    
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
