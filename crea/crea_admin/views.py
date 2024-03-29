from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Cliente, Propiedad

#pagina principal
def index(request):
    template = "index.html"
    return render(request, template)

#pagina clientes
def ver_cliente(request):
    cliente = Cliente.objects.all()
    
    contenido ={
        'cliente': cliente,
    }
    template = "clientes.html"
    return render(request, template, contenido)

#pagina empleados
def ver_empleado(request):
    empleado = Cliente.objects.all()
    
    contenido ={
        'empleado': empleado,
    }
    template = "empleado.html"
    return render(request, template, contenido)

#pagina Propiedades
def ver_propiedades(request):
    propiedad = Propiedad.objects.all()
    contenido = {
        'propiedad' : propiedad
    }
    template = "propiedades.html"
    return render(request, template, contenido)

#pagina Propiedad
def ver_propiedad(request, codigo_propiedad):
    propiedad = Propiedad.objects.get(pk = codigo_propiedad)
    contenido = {
        'propiedad' : propiedad
    }
    template = "propiedad.html"
    return render(request, template, contenido)