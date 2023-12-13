from django import forms
# importamos el model Transaccion para hacer el custom form
from personas.models import Transaccion
# importamos UserCreationForm para poder modificarlo a gusto
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserCreationFormCustom (UserCreationForm):
    # reasignamos los campos del formulario con los nombres que querramos
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [ 'username','email', 'password1', 'password2'] 
        # saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm (UserChangeForm):
    password = None
    email = forms.EmailField(label='Ingrese su email ')
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    edad = forms.IntegerField(label='Edad')

    class Meta():
        model = User
        fields = ['email','last_name','first_name']

# este form sera el form custom para cuando haga la view de ventas
class TransaccionFormCustom (forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['nro_transaccion', 'cliente', 'producto', 'cantidad', 'precio_total', 'fecha_venta']
        # para customizar el campo de fecha_venta:
        widgets = {
            'fecha_venta': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }