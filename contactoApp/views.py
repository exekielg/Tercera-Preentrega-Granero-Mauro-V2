from django.shortcuts import render
from .forms import formcontacto

# Create your views here.

def contacto(request):
        formulario_contacto= formcontacto
        return render(request, 'contactoApp/contacto.html', {'miformulario':formulario_contacto})



