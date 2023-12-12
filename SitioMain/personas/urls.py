from django.urls import path
from personas.views import *
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',register,name='Registro'),
    path('ingresar/',ingresar,name='LogIn'),
    path('logout/',LogoutView.as_view(template_name="logout.html"),name='LogOut'),
    path('crear_perfil/',PerfilUsuarioCreateView.as_view(),name='crear perfil'),
    path('<pk>/editar_perfil/',PerfilUsuarioUpdateView.as_view(),name='editar perfil'),
    path('perfil_usuario/',perfil_usuario,name='ver perfil'),
    path('cambiar_contrasenia/',CambiarContrasenia.as_view(),name='cambiar_contrasenia'),
    
]
