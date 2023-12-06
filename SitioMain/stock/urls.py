from django.urls import path
from stock.views import *

urlpatterns = [
    # urls a las listas de productos (READ)
    path('sabers/',listar_sables,name='sabers'),
    path('crystals/',listar_crystals,name='crystals'),
    path('componentes/',listar_componentes,name='componentes'),
    # urls a agregar  productos (CREATE)
    path('ingresar_sable/',agregar_sable, name='nuevo_sable'),
    path('ingresar_crystal/',agregar_crystal, name='nuevo_crystal'),
    path('ingresar_componente/',agregar_componente, name='nuevo_componente'),
    
]