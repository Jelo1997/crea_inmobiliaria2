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
    fecha_registro = models.DateField()
    ubicacion = models.CharField(max_length=144, blank= False, null= False)
    precio = models.DecimalField(max_digits=65, decimal_places = 2 ,blank = False, null = False)
    tipos = (
        ("Casa", "Casa"),
        ("Terreno", "Terreno"),
    )
    tipo = models.CharField(max_length=15, choices=tipos)  
    descripcion = models.TextField(max_length=500, blank= False, null= False)
   # image = models.ImageField(upload_to="propiedades")
    caracteristicas = models.ManyToManyField(Caracteristicas)
    servicios = models.ManyToManyField(Servicios)
    precio_avaluo = models.DecimalField(max_digits=65, decimal_places = 2 ,blank = False, null = False)
    estados =(
        ("Captar", "Captar"),
        ("Captar Urgente", "Captar Urgente"),
        ("Descartar", "Descartar"),
    )
    estado = models.CharField(max_length=15, choices=estados)  
    
    def __str__(self) -> str:
       return f'{self.tipo, self.precio, self.estado}'
    


class Cliente(models.Model):
    nombre = models.CharField(max_length=144, blank= False, null= False)
    apellido = models.CharField(max_length=144, blank= False, null= False)
    telefono = models.CharField(max_length=144, blank= False, null= False)
    correo = models.EmailField(max_length=144, blank= False, null= False)

    def __str__(self) -> str:
       return f'{self.nombre}'

   
class Empleado(models.Model):
    tipos = (
        ("User", "User"),
        ("Admin", "Admin"),
    )
    tipo = models.CharField(max_length=15, choices=tipos)
    username = models.CharField(max_length=144, blank= False, null= False)
    email  = models.EmailField(max_length=144, blank= False, null= False)
    password = models.CharField(max_length=144, blank= False, null= False)
    telefono = models.CharField(max_length=144, blank= False, null= False)
    
    def __str__(self) -> str:
       return f'{self.tipo}'

    
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

    def __str__(self) -> str:
       return f'{self.nombre}'
    

