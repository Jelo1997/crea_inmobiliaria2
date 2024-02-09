from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Cliente, Propiedad

def index(request):
    template = "index.html"
    return render(request, template)

def ver_cliente(request):
    cliente = Cliente.objects.all()
    
    contenido ={
        'cliente': cliente,
    }
    template = "clientes.html"
    return render(request, template, contenido)
    
def ver_propiedades(request):
    propiedad = Propiedad.objects.all()
    contenido = {
        'propiedad' : propiedad
    }
    template = "propiedades.html"
    return render(request, template, contenido)

def ver_propiedad(request, codigo_propiedad):
    propiedad = Propiedad.objects.get(pk = codigo_propiedad)
    contenido = {
        'propiedad' : propiedad
    }
    template = "propiedad.html"
    return render(request, template, contenido)