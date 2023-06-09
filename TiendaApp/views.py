from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria_Producto, Producto, Cliente
from .forms import ClienteForm, ProductSearchForm, ProductoForm
from django.contrib.auth. forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages





def home(request):
    return render(request, 'TiendaApp/home.html')

# Vista para Agregar nuevos Clientes a la BD
@login_required
def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo cliente en la base de datos
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            direccion =form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, direccion=direccion,telefono=telefono,email=email)
            nuevo_cliente.save()
            return render(request, 'TiendaApp/clientes.html', {'form': form, 'mensaje':'OK'})
    else:
        form = ClienteForm()
    return render(request, 'TiendaApp/clientes.html', {'form': form})


# Tienda de Productos
@login_required
def tienda(request):
    producto = Producto.objects.all()
    return render(request, 'TiendaApp/tienda.html', {"Productos": producto})




# Buscar producto Auto, por marca
@login_required
def buscar_producto(request):
    if request.method == 'POST':
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            p_min = form.cleaned_data['precio_min']
            p_max = form.cleaned_data['precio_max']
            products_qs = Producto.objects.all()
            if marca:
                products_qs = products_qs.filter(marca=marca)
            if modelo:
                products_qs = products_qs.filter(modelo=modelo)
            if p_min:
                products_qs = products_qs.filter(precio__gte=p_min)
            if p_max:
                products_qs = products_qs.filter(precio__lte=p_max)
            products = products_qs.all()
            #return render(request, 'TiendaApp/resultados_busqueda.html', {'marca': marca,'modelo':modelo,'precio_min':p_min,'precio_max':p_max})
    else:
        form = ProductSearchForm()
        products = []

    context = {
        'form': form,
        'products': products,
    }

    return render(request, 'TiendaApp/buscar_producto.html', context)

# Solicitud de Login
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(request,username=usuario, password=contra) # Pasamos la solicitud
            if user is not None:
                login(request,user)
                return render(request, 'TiendaApp/home.html')
            else:
                error_message = "Credenciales Erroneas, intenta de Nuevo."
                return render(request,"TiendaApp/registration/login.html" , {'error_message': error_message})
    else:
        form = AuthenticationForm()
    return render(request,"TiendaApp/registration/login.html", {'form':form})


# Registro de Nuevo Usuario
def register(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        #form m = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "TiendaApp/home.html", {"mensaje": "Usuario Creado con Exito"})
    else:
        form = UserCreationForm()
        #form = UserRegisterForm()
    return render(request, "TiendaApp/registration/registro.html", {"form":form})

# Sale de la Cuenta logeada
def logout_view(request):
    logout(request)
    return redirect('Home')

# Listado de Productos para CRUD
@login_required
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'TiendaApp/productos/producto_list.html', {'productos': productos})


# Crear un nuevo Producto a la BD
@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()

    return render(request, 'TiendaApp/productos/agregar_producto.html', {'form': form})

# Editar un producto de la BD
@login_required
def editar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)

        if form.is_valid():
            form.save()
            messages.success(request, 'PRODUCTO EDITADO.')
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'TiendaApp/productos/editar_producto.html', {'form': form})

# Eliminar un Porducto de la BD
@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    producto.delete()
    messages.success(request, 'PRODUCTO ELIMINADO.')
    return redirect('productos')