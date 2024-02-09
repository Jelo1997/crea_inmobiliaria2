from django.contrib import admin

from .models import Propiedad, Caracteristicas, Servicios, Cliente, Proceso, Empleado

# Register your models here.

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'precio', 'estado')
    
@admin.register(Caracteristicas)
class CaracteristicasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')

@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Proceso)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

