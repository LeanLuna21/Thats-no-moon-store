from django.urls import path
from personas.views import *
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # URLS para usuarios y perfil de usuario
    path('register/',register,name='Registro'),
    path('ingresar/',ingresar,name='LogIn'),
    path('logout/',LogoutView.as_view(template_name="logout.html"),name='LogOut'),
    path('crear_perfil/',PerfilUsuarioCreateView.as_view(),name='crear perfil'),
    # <pk> es el argumento que traemos desde el html que identifica cuál es el usuario cuyo perfil vamos a acceder.
    path('<pk>/editar_perfil/',PerfilUsuarioUpdateView.as_view(),name='editar perfil'),
    path('perfil_usuario/',perfil_usuario,name='ver perfil'),
    path('cambiar_contrasenia/',CambiarContrasenia.as_view(),name='cambiar_contrasenia'),
    
    # URLS vistas ventas
    path('ventas_lista/', TransaccionListView.as_view(), name='listar_ventas'),
    path('ventas_crear/', TransaccionCreateView.as_view(), name='ventas crear'),
    path('<pk>/eliminar/', TransaccionDeleteView.as_view(), name='ventas eliminar'),
    path('<pk>/editar/', TransaccionUpdateView.as_view(), name='ventas editar'),
    path('<pk>/detalle/', TransaccionDetailView.as_view(), name='ventas detalle')
]
