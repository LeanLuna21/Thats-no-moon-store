from django.urls import path
from stock.views import *

urlpatterns = [
    path('sabers/',listar_sabers,name='sabers'),
    path('crystals/',listar_crystals,name='crystals'),
    path('componentes/',listar_componentes,name='componentes'),
]