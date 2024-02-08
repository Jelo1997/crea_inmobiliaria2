from django.contrib import admin
from .models import Propiedad, Caracteristicas, Servicios, Cliente
# Register your models here.

@admin.register(Propiedad)
class CreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    
@admin.register(Caracteristicas)
class CreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Servicios)
class CreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Cliente)
class CreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')