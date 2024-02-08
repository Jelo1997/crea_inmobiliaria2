from django.db import models

# Create your models here.


class Caracteristicas(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    descripcion = models.CharField(max_length=144, blank= False, null= False)

    def __str__(self) -> str:
       return f'{self.nombre}'

class Servicios(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    descripcion = models.CharField(max_length=144, blank= False, null= False)

    def __str__(self) -> str:
       return f'{self.nombre}'
    
class Propiedad(models.Model):
    tipos = (
        ("Casa", "Casa"),
        ("Terreno", "Terreno"),
    )
    tipo = models.CharField(max_length=15, choices=tipos)
    ubicacion = models.CharField(max_length=144, blank= False, null= False)
    precio = models.DecimalField(max_digits= 65, decimal_places = 2 ,blank = False, null = False)
    descripcion = models.TextField(max_length=500, blank= False, null= False)
    #image = models.
    estados = (
            ("Disponible", "Disponible"),
            ("Vendida", "Vendida"),
            ("Reservado", "Reservado"),
            )
        
    estado = models.CharField(max_length=25, choices=estados)
    caracteristicas = models.ManyToManyField(Caracteristicas)
    servicios = models.ManyToManyField(Servicios)

    def __str__(self) -> str:
       return f'{self.tipo}'
    


class Cliente(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    apellido = models.CharField(max_length=144, blank= False, null= False)
    telefono = models.CharField(max_length=144, blank= False, null= False)
    correo = models.EmailField(max_length=144, blank= False, null= False)
    intereses = models.ManyToManyField(Propiedad)

    def __str__(self) -> str:
       return f'{self.nombre}'