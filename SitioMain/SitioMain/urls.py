from django.contrib import admin
from django.urls import path, include
from SitioMain.views import principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal, name="inicio"),
    path('stock/',include('stock.urls')),
    # path('ventas/',include('ventas.urls')),
    # path('personas/',include('personas.urls')),
]
