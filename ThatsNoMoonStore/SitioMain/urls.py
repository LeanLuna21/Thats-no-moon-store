from django.contrib import admin
from django.urls import path, include
from SitioMain.views import principal
#importamos librerias para el manejo de las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal, name="inicio"),
    path('stock/',include('stock.urls')),
    path('personas/',include('personas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
