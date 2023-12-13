from django.db import models
# importamos la clase User para enlazar los perfiles de usuario
from django.contrib.auth.models import User
# importamos los models para conectar con la transaccion (compra)
from stock.models import Producto
# Create your models here.

class PerfilUsuario(models.Model):
    CHOICE = (
        ('Padawan','Padawan'),
        ('Master','Master'),
        ('Lord Sith','Lord Sith')
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,related_name='perfil')
    edad = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenes_usuarios')
    rol = models.CharField(max_length=10,choices=CHOICE, null=True, blank=True)

    def __str__(self):
        return "Usuario: " + self.rol +" "+ self.usuario.username 


# crear MODELO CLIENTE
class Cliente(models.Model):
    nombre = models.ForeignKey(User,on_delete=models.CASCADE,related_name='cliente')
    mail = models.EmailField()
    dni = models.IntegerField()
    direccion = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"Cliente: {self.nombre}."
    
    
# crear MODELO transaccion 
class Transaccion(models.Model):
    nro_transaccion = models.IntegerField() 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name='ventas') # relaciona este modelo con el modelo de clientes
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) # relaciona este modelo con el modelo de productos
    cantidad = models.IntegerField()
    precio_total = models.FloatField() 
    fecha_venta = models.DateField()

    def __str__(self):
        return f"Venta n°: {self.nro_transaccion}."

# prueba para acceder a los valores
# venta = Transaccion.objects.first()
# nombre_cliente = venta.cliente.nombre.user.username
# nombre_producto = venta.producto.nombre