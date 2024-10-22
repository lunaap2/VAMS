from django.db import models

# Create your models here.
class Productos(models.Model):
    CATEGORIAS = [
        ('Collares', 'Collares'),
        ('Aretes', 'Aretes'),
        # Agrega más categorías si es necesario
    ]

    nombre_producto = models.CharField(max_length=100, default='')
    descripcion_producto = models.CharField(max_length=200, default='')
    categoria_producto = models.CharField(max_length=200, choices=CATEGORIAS, default='Collares')
    precio = models.FloatField(default=None)
    disponibilidad = models.IntegerField(default=None)
    producto_vendido = models.IntegerField(default=None)
    imagen_producto = models.ImageField(upload_to='productos/', default='default.jpg')
    
    
class Clientes(models.Model):
    nombre = models,models.CharField(max_length=50, default=None)
    apellido = models,models.CharField(max_length=50, default=None)
    correo_electronico = models,models.CharField(max_length=100, default=None)
    direccion = models,models.CharField(max_length=100, default=None)
    numero_telefono = models,models.CharField(max_length=20, default=None)
    interes = models,models.CharField(max_length=200, default=None)
    
    
class Empleados(models.Model):
    nombre = models,models.CharField(max_length=50, default=None)
    apellido = models,models.CharField(max_length=50, default=None)
    cargo = models,models.CharField(max_length=50, default=None)
    
    
class Factura(models.Model):
     producto = models,models.CharField(max_length=100, default=None)
     cantidad = models.IntegerField(default=None)
     precio_unitario  = models.FloatField(default=None)
     total = models.FloatField(default=None)
     
    
     
    
    
