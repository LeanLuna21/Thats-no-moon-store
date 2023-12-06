from django.db import models

# Creamos los modelos de productos
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    precio = models.FloatField(default=0)
    descripcion = models.TextField()
    

class Sable(Producto):
    color_sable = models.CharField(max_length=50)
    color_luz = models.CharField(max_length=50)
    medida = models.CharField(max_length=10)

    def __str__(self):
        return f"Producto: {self.nombre}."
    
class Crystal(Producto):
    color = models.CharField(max_length=15)
    origen = models.CharField(max_length=20)
    # https://starwars.fandom.com/wiki/Kyber_crystal

class Componente(Producto):
    tipo = models.CharField(max_length=15)  # empuñadura / emisor / etc
    material = models.CharField(max_length=50)  # aleacion / galvanizado / mate / etc
    # https://as.com/meristation/2019/11/27/guia_pagina/1574884260_688289.html
    # https://game8.co/games/Star-Wars-Jedi-Survivor/archives/410234