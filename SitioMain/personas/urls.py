from django.urls import path
from personas.views import *
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',register,name='Registro'),
    path('ingresar/',ingresar,name='LogIn'),
    path('logout/',LogoutView.as_view(template_name="logout.html"),name='LogOut'),
    path('editar_perfil/',editar_perfil,name='editar_perfil'),
    path('cambiar_contrasenia/',CambiarContrasenia.as_view(),name='cambiar_contrasenia'),

]
