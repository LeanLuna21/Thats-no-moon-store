from django.http import HttpResponse
from django.shortcuts import render

# acá voy a agregar las fx para modificar el template
# crear fx que rendericen las htm
def principal(request):
    return render(request, './index.html')
