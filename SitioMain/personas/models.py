from django.db import models
# importamos la clase User para enlazar los perfiles de usuario
from django.contrib.auth.models import User
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


