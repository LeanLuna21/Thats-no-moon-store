from django.shortcuts import render
from django.http import HttpResponse
# importar forms para registro y login
from personas.forms import UserCreationFormCustom, UserEditForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# este modulo lo usaremos para cambiar la contraseña
from django.contrib.auth.views import PasswordChangeView
# este modulo lo usaremos para obligar al usuario a logearse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# este modulo se usa para usar las VIEW de django por defecto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# VIEWS para registrarse e ingresar. (CREATE)

def register (request):
    if request.method  == 'POST':

        new_form = UserCreationFormCustom(request.POST)
        if new_form.is_valid():
            username = new_form.cleaned_data['username']
            new_form.save()
            return render(request,'index.html',{'mensaje':f'Usuario creado! Te damos la bienvenida Joven Padawan {username}!'})

    else:
        new_form = UserCreationFormCustom()
    return render(request,'registro.html',{"mi_formulario":new_form})
    
def ingresar (request):
    if request.method  == 'POST':

        new_form = AuthenticationForm(request, data=request.POST)
        if new_form.is_valid():
            usuario = new_form.cleaned_data.get('username')
            contrasenia = new_form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            login(request,user)

            return render(request, 'index.html',{'mensaje':f'Bienvenido Padawan {user.username}'})
    
    else:
        new_form = AuthenticationForm()
    return render(request,'login.html',{"mi_formulario":new_form})

# VIEW para editar usuario (UPDATE) 
def editar_perfil(request):
    # muestra quien esta logeado
    usuario = request.user
    
    if request.method == 'POST':
        new_form = UserEditForm(request.POST, instance=request.user)

        if new_form.is_valid():
            new_form.save()

            return render(request, 'index.html')

    else:
        # mostramos el formulario con los datos iniciales (los existentes)
        new_form = UserEditForm(initial={'email':usuario.email,'last_name':usuario.last_name,'first_name':usuario.first_name})
    
    return render(request, 'perfil-editar.html',{"mi_formulario":new_form,"usuario":usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cambiar_contrasenia.html'
    success_url = reverse_lazy('editar_perfil')