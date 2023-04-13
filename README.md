# ENTREGA DE PROYECTO FINAL 


* se realizaron las Views con herencia y modelos de datos que permiten persistencia de los datos dentro de las BD
* NavBar con 
Inicio
Tienda
Buscar
Clientes
Registrar
Contacto
Productos
* Apps de Carrito, TiendaApp, Contacto y CRUD
* TiendaApp es la que contiene las vistas principales de Tienda, Buscar, Clientes, Registrar asi como el Login/logout, 
* Contacto es una App a parte para enviar mensajes persistentes en la un model de la App, se pueden examinar desde el Admin
* desde Productos se puede realizar un CRUD completo en la BD de productos
* Django widget_tweaks a los formularios se le agregaron estilos con esta App
      Instalar:   $ pip install django-widget-tweaks

        INSTALLED_APPS += [
            'widget_tweaks',
        ]

* El formulario Clientes, sirve para agregar un nuevo cliente a la BD
* El formulario Buscar realiza una busqueda dentro de la base de Productos de la tienda
* Registrar registra un nuevo usuario con nombre y pass
* Se protegieron las vistas sensibles con el decorator @login_required
* en la esquina superior se agrego un boton de login que cambia a salir cuando uno se encuentra logueado y muestra en la misma barra nombre del user
* se Creo una App de Carro que se basa en los datos de sesion actual, es decir que los items agregados al carro se borran al salir de la sesion, para ello se utilizo un context processor que administra las sesiones y se pulio la funcion AGREGAR (estan pendientes las demas funciones para que el carro pueda ser funcional)
* la tienda cuenta con imagenes y detalles de cada producto y todos los botones son funcionales.




