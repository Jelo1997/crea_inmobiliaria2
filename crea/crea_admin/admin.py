from django.contrib import admin
from .models import Propiedad, Caracteristicas, Servicios, Cliente
# Register your models here.

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    
@admin.register(Caracteristicas)
class CaracteristicasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')