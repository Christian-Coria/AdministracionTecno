from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models import Model



class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    
    def __str__(self):
        return f'Nombre {self.nombre} {self.apellido} {self.telefono} '


class Repuestos(models.Model):
    clase = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f'Clase {self.clase}: {self.marca} {self.modelo} {self.precio} {self.stock}'


class Accesorios(models.Model):
    clase = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return f'Clase {self.clase}: {self.marca} {self.modelo} {self.precio} {self.stock} '


class Herramientas(models.Model):
    clase = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()
    
    def __str__(self):
        return f'Clase {self.clase}: {self.marca} {self.precio} {self.stock}'


class Proveedores(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
   
    def __str__(self):
        return f'Proveedor {self.nombre}: {self.telefono}'


MARCA = (
    ('Motorola','Motorola'),
    ('Samsung','Samsung'),
    ('Lg','Lg'),
    ('Xiaomi','Xiaomi'),
    ('Sony','Sony'),
    ('Huawey','Huawey'),
    ('Chino','Chino'),
    ('Otro','Otro'),
)
ESTADO = (
    ('Pendiente','Pendiente'),
    ('Aceptado','Aceptado'),
    ('Reparado','Reparado'),
    ('Irreparable','Irreparable'),
    ('Entregado','Entregado'),
    ('Entregado Irreparable','Entregado Irreparable'),
    
)


class IngresoTecnico(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente,null=True, on_delete=models.CASCADE)
    marca = models.CharField(max_length=40, choices=MARCA)
    modelo = models.CharField(max_length=40)
    imei = models.CharField(max_length=40)
    accesorios = models.CharField(max_length=40)
    falla = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="fallas", null=True, blank=True)
    comentarios = RichTextField()
    precio = models.IntegerField()
    

def __str__(self):
        return f'Orden de Ingreso: {self.fecha} {self.marca} {self.modelo} {self.imei} {self.accesorios} {self.falla} {self.imagen} {self.comentarios} {self.precio} '


class TareasPendientes(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion= models.TextField(blank=True)
    estado = models.CharField(max_length=40)


class Reparacion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=40,blank=True )
    marca = models.CharField(max_length=40, choices=MARCA)
    modelo = models.CharField(max_length=40, blank=True)
    imei = models.CharField(max_length=40,blank=True )
    falla = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to="fallas", null=True, blank=True)
    comentarios = RichTextField(null=True)
    presupuesto = models.IntegerField(null=True ,blank=True)
    precio = models.IntegerField()
    estado = models.CharField(max_length=40, choices=ESTADO)
    

def __str__(self):
        return f'Orden de Ingreso: {self.fecha} {self.cliente} {self.telefono} {self.marca} {self.modelo} {self.imei} {self.falla} {self.imagen} {self.comentarios}  {self.presupuesto} {self.precio} {self.estado}'

