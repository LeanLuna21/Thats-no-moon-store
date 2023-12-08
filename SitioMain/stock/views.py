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
def editar_sable(request,sable_nombre):
    # obtenemos el objeto que coincide con el nombre a editar y lo guardamos en una variable
    sable = Sable.objects.get(nombre=sable_nombre)
    
    if request.method == 'POST':
        
        new_form = SableFormulario(request.POST)

        if new_form.is_valid():

            data = new_form.cleaned_data
            # llamamos a los campos del objeto y los enlazamos con la informacion traida del formulario
            sable.nombre=data['nombre']     
            sable.stock=data['stock']        
            sable.precio=data['precio']
            sable.descripcion= data['descripcion']
            sable.medida= data['medida']
            sable.color_sable= data['color_sable']
            sable.color_luz= data['color_luz']
            

            sable.save() # guardamos los cambios
            return render(request,'index.html') # regresamos donde deseemos

    # si no ingresa a la fx por el metodo POST, devolvemos el formulario con los campos del form llenos    
    else:
        new_form = SableFormulario(initial={"nombre":sable.nombre,"stock":sable.stock,"precio":sable.precio,"descripcion":sable.descripcion,"medida":sable.medida,"color_sable":sable.color_sable,"color_luz":sable.color_luz})

        return render(request,'producto_edit.html',{"mi_formulario":new_form})


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
def editar_crystal(request,crystal_nombre, crystal_color):
    # obtenemos el objeto que coincide con el nombre a editar y lo guardamos en una variable
    crystal = Crystal.objects.get(nombre=crystal_nombre,color=crystal_color)
    
    if request.method == 'POST':
        
        new_form = CrystalFormulario(request.POST)

        if new_form.is_valid():

            data = new_form.cleaned_data
            # llamamos a los campos del objeto y los enlazamos con la informacion traida del formulario
            crystal.nombre=data['nombre'] 
            crystal.tipo= data['tipo']   
            crystal.color= data['color']
            crystal.origen= data['origen'] 
            crystal.stock=data['stock']        
            crystal.precio=data['precio']
            crystal.descripcion= data['descripcion']

            crystal.save() # guardamos los cambios
            return render(request,'index.html') # regresamos donde deseemos

    # si no ingresa a la fx por el metodo POST, devolvemos el formulario con los campos del form llenos    
    else:
        new_form = CrystalFormulario(initial={"nombre":crystal.nombre,"tipo":'Kyber Crystal',"color":crystal.color,"origen":crystal.origen,"stock":crystal.stock,"precio":crystal.precio,"descripcion":crystal.descripcion})

        return render(request,'producto_edit.html',{"mi_formulario":new_form})

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
def editar_componente(request,componente_tipo, componente_nombre):
    # obtenemos el objeto que coincide con el nombre a editar y lo guardamos en una variable
    componente = Componente.objects.get(tipo=componente_tipo, nombre=componente_nombre)
    
    if request.method == 'POST':
        
        new_form = ComponenteFormulario(request.POST)

        if new_form.is_valid():

            data = new_form.cleaned_data
            # llamamos a los campos del objeto y los enlazamos con la informacion traida del formulario
            componente.tipo= data['tipo']
            componente.nombre=data['nombre']
            componente.material= data['material']     
            componente.stock=data['stock']        
            componente.precio=data['precio']
            componente.descripcion= data['descripcion']
            

            componente.save() # guardamos los cambios
            return render(request,'index.html') # regresamos donde deseemos

    # si no ingresa a la fx por el metodo POST, devolvemos el formulario con los campos del form llenos    
    else:
        new_form = ComponenteFormulario(initial={"tipo":componente.tipo,"nombre":componente.nombre,"material":componente.material,"stock":componente.stock,"precio":componente.precio,"descripcion":componente.descripcion})

        return render(request,'producto_edit.html',{"mi_formulario":new_form})

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

        producto = Producto.objects.filter(nombre__icontains=nombre)
        return render(request,'resultados_busqueda.html',{'producto':producto})
    else:
        return render(request,'resultados_busqueda.html')