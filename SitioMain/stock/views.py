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
    
    sabers = Sable.objects.all() #trae todos los objects(instancias de la clase) 
    contexto = {"productos":sabers}  #creamos el diccionario a renderizar -> cada valor se vera 
    
    return render(request,'sabers.html', contexto)

# C
def crear_sable(request):

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
            return render(request,'index.html') # podemos crear un html de "producto agregado!"

    else:
        new_form = SableFormulario()
        return render(request,'saber_create.html',{"mi_formulario":new_form})

# U
def editar_sable():
    ...

# D
def eliminar_sable(request,sable_nombre): # traemos el parametro tomado al momento de apretar boton eliminar
    # obtenemos el objeto que coincida con el nombre
    sable = Sable.objects.get(nombre=sable_nombre)
    # lo borramos
    sable.delete()
    
    # volvemos a mostrar los productos que quedaron
    sabers = Sable.objects.all() # trae todos los sabels que quedaron

    # la variable producto es la que se itera en el html
    contexto= {"productos":sabers} 

    return render(request,"sabers.html",contexto)
   




##### CRUD crystals #####
def listar_crystals(request):
    crystals = Crystal.objects.all() #trae todos los objects(instancias de la clase) 
    contexto = {"productos":crystals}  #creamos el diccionario a renderizar -> cada valor se vera 
    
    return render(request, 'crystals.html', contexto)

# C
def crear_crystal(request):

    if request.method == 'POST':
        new_form = CrystalFormulario(request.POST)
        if new_form.is_valid():
            data = new_form.cleaned_data

            producto = Crystal(       
                nombre=data['nombre'],      # asigno a cada atributo del objeto, el valor almacenado 
                color= data['color'],       # en la clave del diccionario "data"
                origen= data['origen'],
                stock=data['stock'],        
                precio=data['precio'],
                descripcion= data['descripcion']
            )

            producto.save() # guardamos el objeto creado en la BBDD
            return render(request,'index.html') # recargamos la pag principal

    else:
        new_form = CrystalFormulario()
        return render(request,'crystal_create.html',{"mi_formulario":new_form})

# U
def editar_crystal():
    ...

# D
def eliminar_crystal(request, crystal_nombre, crystal_color): # traemos el parametro tomado al momento de apretar boton eliminar
    # obtenemos el objeto que coincida con el nombre
    crystal = Crystal.objects.get(nombre=crystal_nombre,color=crystal_color)
    # lo borramos
    crystal.delete()
    
    # volvemos a mostrar los productos que quedaron
    crystals = Crystal.objects.all() # trae todos los cristales que quedaron

    # la variable producto es la que se itera en el html
    contexto= {"productos":crystals} 

    return render(request, "crystals.html",contexto)  

##### CRUD componentes #####
def listar_componentes(request):
    componentes = Componente.objects.all() #trae todos los objects(instancias de la clase) 
    contexto = {"productos":componentes}  #creamos el diccionario a renderizar -> cada valor se vera 
    
    return render(request, 'componentes.html',contexto)

# C
def crear_componente(request):

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
            return render(request,'index.html') 

    else:
        new_form = ComponenteFormulario()
        return render(request,'component_create.html',{"mi_formulario":new_form})

# U
def editar_componente():
    ...

# D
def eliminar_componente(request, componente_tipo, componente_nombre): # traemos el parametro tomado al momento de apretar boton eliminar
    # obtenemos el objeto que coincida con el nombre
    componente = Componente.objects.get(tipo=componente_tipo, nombre=componente_nombre)
    # lo borramos
    componente.delete()
    
    # volvemos a mostrar los productos que quedaron
    componentes = Componente.objects.all() # trae todos los componentes que quedaron

    # la variable producto es la que se itera en el html
    contexto= {"productos":componentes} 

    return render(request, "componentes.html",contexto) 


################# fx varias #################
def mostrar_productos(request):
    lista_productos  = Producto.objects.all()
   
    return render(request, 'nuestros_productos.html', {'lista':lista_productos})

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre'] # Rey
        # filtra la bbdd 

        # try:
        producto = Producto.objects.filter(nombre__icontains=nombre)
        return render(request,'resultados_busqueda.html',{'producto':producto})
        # except:
        #     producto = 0
        #     return render(request,'resultados_busqueda.html',{'producto':producto})

        # try-except no funciona aca porque siempre filtra, pero a veces devulve coincidencia y si no vacio - pero simpre devuelve
