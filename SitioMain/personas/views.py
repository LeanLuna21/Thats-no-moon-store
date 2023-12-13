from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# importar forms para registro y login
from personas.models import PerfilUsuario, Cliente, Transaccion
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
from django.contrib.auth.decorators import login_required
# VIEWS para registrarse e ingresar. (CREATE)

def register (request):
    
    if request.method  == 'POST':
        new_form = UserCreationFormCustom(request.POST)
        
        if new_form.is_valid():
            username = new_form.cleaned_data['username']
            new_form.save()
            return render(request,'index.html',{'mensaje':f'Usuario creado! Te damos la bienvenida Joven Padawan {username}!'})
        
        else:
            return render(request,'registro.html',{"mi_formulario":new_form})
    
    else:
        new_form = UserCreationFormCustom()
        return render(request,'registro.html',{"mi_formulario":new_form})
    

def ingresar (request):
    
    if request.method  == 'POST':
        new_form = AuthenticationForm(request, data=request.POST)
        
        if new_form.is_valid():
            usuario = new_form.cleaned_data.get('username')
            contrasenia = new_form.cleaned_data.get('password')
            # fx importadas para no codearlo nosotros 
            user = authenticate(username=usuario, password=contrasenia)
            # si la authenticate fx es valida, django sabe que entramos con un user registrado
            login(request,user) # y lo logea
            return render(request, 'index.html',{'mensaje':f'Bienvenido Padawan {user.username}'})
        
        else:
            return render(request,'login.html',{"mi_formulario":new_form})
    
    else:
        new_form = AuthenticationForm()
        return render(request,'login.html',{"mi_formulario":new_form})


#creo la vista del perfil
class PerfilUsuarioCreateView(LoginRequiredMixin, CreateView):
    # model a trabajar
    model = PerfilUsuario    
    # archivo a renderizar
    template_name = 'crear_perfil.html'
    # redirigirme a ... una vez creado el perfil de forma exitosa
    success_url = reverse_lazy ('ver perfil')
    # campos del model a completar
    fields = ['usuario','imagen', 'rol', 'edad']


class PerfilUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = PerfilUsuario    
    template_name = 'editar_perfil.html'
    success_url = reverse_lazy ('ver perfil')
    fields = ['imagen','edad', 'rol']


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'cambiar_contrasenia.html'
    success_url = reverse_lazy('ver perfil')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Contraseña cambiada exitosamente.')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Hubo un problema al cambiar la contraseña. Por favor, inténtalo de nuevo.')
        return response

@login_required(login_url='LogIn')
def perfil_usuario(request):
    try:
        request.user.perfil
        return render(request, 'perfil.html')
    except:
        return redirect('crear perfil')
    
###########################################################  
    #  Vistas VENTAS (transacciones)
class TransaccionListView(ListView):
    model = Transaccion
    context_object_name = "ventas"
    template_name = "listar_ventas.html"

class TransaccionCreateView(CreateView):
    model = Transaccion
    template_name = "crear_venta.html"
    success_url = reverse_lazy('listar_ventas')
    fields = ['nro_transaccion', 'cliente', 'producto', 'cantidad' ,'precio_total', 'fecha_venta']

class TransaccionUpdateView(UpdateView):
    model = Transaccion
    template_name = "editar_ventas.html"
    success_url = reverse_lazy("listar_ventas")
    fields = ['producto', 'cantidad','precio_total','fecha_venta']

class TransaccionDeleteView(DeleteView):
    model = Transaccion
    template_name = "eliminar_ventas.html"
    success_url = reverse_lazy("listar_ventas")

class TransaccionDetailView(DetailView):
    model = Transaccion
    template_name = "detalle_ventas.html"
    success_url = reverse_lazy("listar_ventas")