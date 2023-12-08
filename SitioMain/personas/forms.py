from django import forms
# importamos UserCreationForm para poder modificarlo a gusto
from django.contrib.auth.forms import UserCreationForm, UserModel


class UserCreationFormCustom (UserCreationForm):
    # reasignamos los campos del formulario con los nombres que querramos
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = UserModel
        fields = [ 'username','email', 'password1', 'password2'] 
        # saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
