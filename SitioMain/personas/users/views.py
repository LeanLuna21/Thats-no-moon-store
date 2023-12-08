from django.shortcuts import render
from django.http import HttpResponse
# importar forms para registro y login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from personas.forms import UserCreationFormCustom

# Create your views here.
