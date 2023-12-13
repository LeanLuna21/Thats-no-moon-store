from django.contrib import admin
from personas.models import PerfilUsuario,Cliente,Transaccion
# Register your models here.
admin.site.register(PerfilUsuario)
admin.site.register(Cliente)
admin.site.register(Transaccion)