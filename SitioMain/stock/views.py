from django.shortcuts import render
from django.http import HttpResponse

# conectamos con los productos
from stock.models import Producto

# Create your views here.
def listar_sabers(request):
    return render(request, './sabers.html')

def listar_crystals(request):
    return render(request, './crystals.html')

def listar_componentes(request):
    return render(request, './componentes.html')