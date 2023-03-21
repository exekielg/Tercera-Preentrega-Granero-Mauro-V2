from django.contrib import admin

# Register your models here.
from .models import Categoria_Producto, Producto, Cliente

#Asignar ReadOnly
class Cat_Prod_Admin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

class Prod_Admin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

class Cliente_Admin(admin.ModelAdmin):
    readonly_fields=("created", "updated")

#registrtrados
admin.site.register(Categoria_Producto, Cat_Prod_Admin)

admin.site.register(Producto, Prod_Admin)

admin.site.register(Cliente, Cliente_Admin)


