# ThatsNoMoonStore
## Tienda online de LightSabers

Para poder ejecutar el proyecto será necesario:

- 1 - Hacer una copia de este repositorio o en su defecto descargarlo como archivo comprimido ZIP.
- 2 - Descomprimirlo y abrirlo con VSC o en el entorno de preferencia.
- 3 - Abrir una terminal e instalar los paquetes necesarios (se recomienda crear un virtual environment previamente) ejecutando el comando 'pip install -r requirements.txt' dentro de la carpeta donde se encuentre ese archivo.
- 4 - Dirigirse a la carpeta donde esta almacenado el documento "manage.py" (/SitioMain)
- 5 - Ejecutar el comando 'python manage.py runserver' para ver el proyecto

Una vez realizados estos pasos debería mostrarse el sitio en el navegador. 

En esta simulacion de tienda. Los usuarios podran registrarse, para comprar diferentes productos: Lightsabers, Cristales para sus lightsabers, o Componentes para construir sus propios sables. 

El sitio esta diseñado para mostrar toda la lista de productos, y poder buscar algun personaje que el usuario desee; lo cual arrojara como resultado el stock que coincida o un mensaje de "no hay stock".

Hasta el momento hay dos usuarios de prueba registrados: el ADMIN y un usuario random que no es parte del staff
Para acceder como admin:
    user: admin
    passw: admincontra1
Para probar la vista desde otro usuario pueden ingresar con:
    user: usuario1
    passw: userpass123

Si no, pueden registrarse con un usuario propio.

Al loguearse con el usuario admin, la vista del sitio cambia (en la navbar se mostraran cada modelo de productos, cada uno con su detalle, y botones para agregar, editar, o borrar registros)

La idea es que solo el admin pueda realizar cambios en la BBDD.

Luego, desde el boton perfil, cada usuario puede crearse un perfil, o editar el que ya tenga creado.
Podran ahi agregar imagenes, modificar sus datos y cambiar su contraseña si asi lo desean. 

PARA VER COMO FUNCIONA EL SITIO:
https://www.youtube.com/watch?v=p1VN8ZjaFQ0&ab_channel=LeandroLuna

COSAS POR MEJORAR:
- primero que nada, habria que agregar el tema de manejo de errores para que, por ej, el stock no se muestre negativo; o directamente no se muestre el producto sin stock
- boton 'comprar producto' deberia generar una instancia de Transaccion donde se guarden los datos del cliente, el producto, la cantidad y el precio
- cada producto podria mostrarse con una imagen para hacer mas atractivo el sitio
- por ultimo el orden en las apps se podria mejorar montones: organizar los html en carpetas, por ej...

ERRORES POR CORREGIR:
- en boton buscar - si no hay coincidencias, mostrar que no hay stock (se muestra vacio).
- en editar perfil - mje de contraseña 'success' o 'fail' se muestra varias veces.
- las imagenes en los productos solo pueden cargarse desde el sitio de admin django, no logro hacer que se puedan subir desde el html de saber_create (ImageField en form esta fallando?)

