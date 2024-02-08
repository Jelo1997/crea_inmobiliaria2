from django.db import models

# Create your models here.

class propiedad(models.Model):
    tipos = {
        "Casa": "Casa",
        "Terreno": "Terreno",
    }
    tipo = models.CharField(max_length=15, choices=tipos)
    ubicacion = models.CharField(max_length=144, blank= False, null= False)
    precio = models.DecimalField(blank = False, null = False)
    descripcion = models.TextField(max_length=500, blank= False, null= False)
    #image = models.
    estados = {
            "Disponible": "Disponible",
            "Vendida": "Vendida",
            "Reservado": "Reservado",
        }
    estado = models.CharField(max_length=25, choices=estados)
    caracteristicas = models.ManyToManyField(caracteristicas)
    servicios = models.ManyToManyField(servicios)

    def __str__(self) -> str:
       return f'{self.tipo}'
    
class caracteristicas(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    descripcion = models.CharField(max_length=144, blank= False, null= False)

    def __str__(self) -> str:
       return f'{self.nombre}'

class servicios(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    descripcion = models.CharField(max_length=144, blank= False, null= False)

    def __str__(self) -> str:
       return f'{self.nombre}'

class cliente(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    apellido = models.CharField(max_length=144, blank= False, null= False)
    telefono = models.CharField(max_length=144, blank= False, null= False)
    correo = models.EmailField(max_length=144, blank= False, null= False)
    intereses = models.ManyToManyField(propiedad)
    
    def __str__(self) -> str:
       return f'{self.nombre}'