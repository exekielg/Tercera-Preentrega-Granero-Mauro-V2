from django.shortcuts import render, redirect
from .forms import formcontacto

# Create your views here.

def contacto(request):
        formulario_contacto= formcontacto
        if request.method=="POST":
                formulario_contacto=formcontacto(data= request.POST)
                formulario_contacto.is_valid()
                nombre=request.POST.get("Nombre")
                cel=request.POST.get("Celular")
                email=request.POST.get("Email")
                mensaje=request.POST.get("Mensaje")

                return redirect("/contacto/?okmensaje")


                
        
        


        return render(request, 'contactoApp/contacto.html', {'miformulario':formulario_contacto})




