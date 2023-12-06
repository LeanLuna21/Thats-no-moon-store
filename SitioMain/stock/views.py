from django.shortcuts import render
from django.http import HttpResponse

# conectamos con los productos
from stock.models import Producto,Sable,Crystal,Componente
# conectamos con los formularios
from stock.forms import SableFormulario, CrystalFormulario, ComponenteFormulario
# Create your views here.

##### CRUD sabers #####
# R
def listar_sables(request):
    return render(request, './sabers.html')

# C
def agregar_sable(request):

    if request.method == 'POST':
        new_form = SableFormulario(request.POST)
        if new_form.is_valid():
            data = new_form.cleaned_data

            producto = Sable(       
                nombre=data['nombre'],      # asigno a cada atributo del objeto, el valor almacenado 
                stock=data['stock'],        # en la clave del diccionario "data"
                precio=data['precio'],
                descripcion= data['descripcion'],
                medida= data['medida'],
                color_sable= data['color_sable'],
                color_luz= data['color_luz']
            )

            producto.save() # guardamos el objeto creado en la BBDD
            return render(request,'sabers.html') # recargamos la pag principal

    else:
        new_form = SableFormulario()
        return render(request,'saber_add.html',{"mi_formulario":new_form})

# U
def editar_sable():
    ...

# D
def eliminar_sable():
    ...   




##### CRUD crystals #####
def listar_crystals(request):
    return render(request, './crystals.html')

# C
def agregar_crystal(request):

    if request.method == 'POST':
        new_form = CrystalFormulario(request.POST)
        if new_form.is_valid():
            data = new_form.cleaned_data

            producto = Crystal(       
                nombre=data['nombre'],      # asigno a cada atributo del objeto, el valor almacenado 
                color= data['color'],
                origen= data['origen'],
                stock=data['stock'],        # en la clave del diccionario "data"
                precio=data['precio'],
                descripcion= data['descripcion']
            )

            producto.save() # guardamos el objeto creado en la BBDD
            return render(request,'crystals.html') # recargamos la pag principal

    else:
        new_form = CrystalFormulario()
        return render(request,'crystal_add.html',{"mi_formulario":new_form})

# U
def editar_crystal():
    ...

# D
def eliminar_crystal():
    ...  

##### CRUD componentes #####
def listar_componentes(request):
    return render(request, './componentes.html')

# C
def agregar_componente(request):

    if request.method == 'POST':
        new_form = ComponenteFormulario(request.POST)
        if new_form.is_valid():
            data = new_form.cleaned_data

            producto = Componente(       
                tipo= data['tipo'],
                nombre=data['nombre'],      
                material= data['material'],
                stock=data['stock'],        
                precio=data['precio'],
                descripcion= data['descripcion'],
            )

            producto.save() 
            return render(request,'componentes.html') 

    else:
        new_form = ComponenteFormulario()
        return render(request,'component_add.html',{"mi_formulario":new_form})

# U
def editar_componente():
    ...

# D
def eliminar_componente():
    ...  


################# fx varias #################
