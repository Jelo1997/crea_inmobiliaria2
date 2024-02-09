from django.db import models

# Create your models here.


class Caracteristicas(models.Model):
    caract = (
            ("Habitaciones", "Habitaciones"),
            ("Baños", "Baños"),
            ("Patio", "Patio"),
            ("Piscina", "Piscina"),
            )
    nombre = models.CharField(max_length=15, choices=caract)
    descripcion = models.CharField(max_length=144, blank= False, null= False)

    def __str__(self) -> str:
       return f'{self.nombre, self.descripcion}'

class Servicios(models.Model):

    serv = (
            ("Internet", "Internet"),
            ("Luz", "Luz"),
            ("Agua", "Agua"),
            ("Alcantarillado", "Alcantarillado"),
            )
    nombre = models.CharField(max_length=15, choices=serv)
    descripcion = models.CharField(max_length=144, blank= False, null= False)

    def __str__(self) -> str:
       return f'{self.nombre, self.descripcion}'
    
class Propiedad(models.Model):
    tipos = (
        ("Casa", "Casa"),
        ("Terreno", "Terreno"),
    )
    tipo = models.CharField(max_length=15, choices=tipos)
    ubicacion = models.CharField(max_length=144, blank= False, null= False)
    precio = models.DecimalField(max_digits=65, decimal_places = 2 ,blank = False, null = False)
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
       return f'{self.tipo, self.precio, self.estado}'
    


class Cliente(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    apellido = models.CharField(max_length=144, blank= False, null= False)
    telefono = models.CharField(max_length=144, blank= False, null= False)
    correo = models.EmailField(max_length=144, blank= False, null= False)
    intereses = models.ManyToManyField(Propiedad)

    def __str__(self) -> str:
       return f'{self.nombre}'
    
class Proceso(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    descripcion = models.CharField(max_length=144, blank= False, null= False)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estados= (
            ("En Curso", "En Curso"),
            ("Finalizado", "Finalizado"),
            )
    estado = models.CharField(max_length=25, choices=estados)
    cliente = models.ForeignKey(Cliente, related_name = 'pk', on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, related_name = 'pk', on_delete=models.CASCADE)
    agente = models.ForeignKey() 
    