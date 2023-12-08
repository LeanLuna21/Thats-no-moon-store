from django.shortcuts import render
from django.http import HttpResponse
# importar forms para registro y login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from personas.forms import UserCreationFormCustom

# Create your views here.

def register (request):
    if request.method  == 'POST':

        new_form = UserCreationFormCustom(request.POST)
        if new_form.is_valid():
            username = new_form.cleaned_data['username']
            new_form.save()
            return render(request,'index.html',{'mensaje':'Usuario creado EXITOSAMENTE! Te damos la bienvenida Joven Padawan!'})

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
    