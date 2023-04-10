from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ContactoForm

# Vista para enviar Mesaje de Contacto a la Empresa se graba en BD
@login_required
def nuevo_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contactoApp/nuevo_contacto.html', {'form': form, 'mensaje':'OK'})
    else:
        form = ContactoForm()

    return render(request, 'contactoApp/nuevo_contacto.html', {'form': form})






