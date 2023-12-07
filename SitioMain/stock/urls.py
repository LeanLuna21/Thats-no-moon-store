from django.urls import path
from stock.views import *

urlpatterns = [
    # url a la lista de productos completa
    path('nuestros_productos/',mostrar_productos, name='nuestros_productos'),
    path('buscar_producto/',buscar, name='buscar_producto'),
    # urls a las listas de productos (READ)
    path('sabers/',listar_sables,name='sabers'),
    path('crystals/',listar_crystals,name='crystals'),
    path('componentes/',listar_componentes,name='componentes'),

    # urls a agregar  productos (CREATE)
    path('crear_sable/',crear_sable, name='crear_sable'),
    path('crear_crystal/',crear_crystal, name='crear_crystal'),
    path('crear_componente/',crear_componente, name='crear_componente'),

    # urls a editar productors (UPDATE)
    path('saber_edit/<sable_nombre>',editar_sable,name='editar_sable'),

    # urls a eliminar productors (DELETE)
    path('eliminar_sable/<sable_nombre>',eliminar_sable,name='eliminar_sable'),
]