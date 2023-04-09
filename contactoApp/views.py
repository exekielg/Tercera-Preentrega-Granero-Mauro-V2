from django.shortcuts import render, redirect
from .forms import ContactoForm


def nuevo_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contactoApp/nuevo_contacto.html', {'form': form, 'mensaje':'OK'})
    else:
        form = ContactoForm()

    return render(request, 'contactoApp/nuevo_contacto.html', {'form': form})






