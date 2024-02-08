from django.contrib import admin
from .models import propiedad, caracteristicas, servicios, cliente
# Register your models here.

@admin.register(propiedad)
class CreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    
@admin.register(caracteristicas)
class CreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(servicios)
class CreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(cliente)
class CreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')