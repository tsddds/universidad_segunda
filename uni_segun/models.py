
from django.db import models
from django.contrib.auth.models import User

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=255)
    

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    academia = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    numero_de_telefono = models.CharField(max_length=15, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class CarroCompra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return f"Carro de {self.usuario.nombre} {self.usuario.apellido}"

class Tarjetas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(max_length=16)
    fecha_expiracion = models.DateField()
    codigo_seguridad = models.CharField(max_length=4)
    tipo_tarjeta = models.CharField(max_length=50)
    nombre_tarjeta = models.CharField(max_length=225)

    def __str__(self):
        return f"Tarjeta de {self.usuario.nombre} {self.usuario.apellido}"

class Direcciones(models.Model):
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.direccion
