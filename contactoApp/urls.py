from django.urls import path
from contactoApp import views



urlpatterns = [
    path('nuevo_contacto', views.nuevo_contacto, name='Contacto'),
    
]

