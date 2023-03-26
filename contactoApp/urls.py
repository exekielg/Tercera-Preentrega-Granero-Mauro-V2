from django.urls import path
from contactoApp import views



urlpatterns = [
    path('contacto/',views.contacto, name='Contacto'),
    
]

