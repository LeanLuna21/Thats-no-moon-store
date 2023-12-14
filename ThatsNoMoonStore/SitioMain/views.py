from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# acá voy a agregar las fx para modificar el template
# crear fx que rendericen las htm

@login_required
def principal(request):
    return render(request,'index.html')
