from django.contrib import admin

# registramos los modelos (impacta en la bbdd)
from stock.models import Sable,Componente,Crystal

admin.site.register(Sable)
admin.site.register(Componente)
admin.site.register(Crystal)