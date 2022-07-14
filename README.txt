ENTREGA INTERMEDIA DEL PROYECTO FINAL
Plataforma: Coderhouse
Grupo conformado por:
- Sergio Andrade
- Tomas Ruiz
- Tadeo Medinilla

Tema: En el proyecto desarrollamos una pagina web sobre la F1 donde los usuarios pogran registrarse y acceder a informacion
segun la clase a la que pertenezcan.

En el siguiente documento se detalla:

1) Como probar el proyecto. 
2) Aproximadamente los pasos que seguimos para armar la aplicacion. 

---------------------------------------------------------------------------------------------------------------------

COMO PROBAR EL PROYECTO

Se le suministro una direccion que lo redirigira al repositorio donde estan guardadas todas las carpetas
que contienen el proyecto y que son necesarias para el correcto funcionamiento. En caso de no tener dicho link 
lo adjuntamos nuevamente. Link al repositorio: https://github.com/TadeoMedinilla/Proyecto.git

De dicho repositorio descargue el archivo ZIP y descomprimalo en alguna carpeta. 
Abra la carpeta con Visual Studio Code. Estando parado en esa carpeta abra el terminal y ejecute la siguiente linea:

python manage.py runserver

Al realizar esto el terminal le proporcionara un link que lo redirigira al sitio web que desarrollamos. Al ingresar 
se encontrara con una pagina de inicio, con una barra de navegacion en la parte superior, si hace click en cualquiera
de los botones de esta barra lo redirigira a la seccion que corresponda, sea dentro de la pagina o en un link anexado.

A continuacion detallaremos lo que se encuentra en cada carpeta, lo que hay en cada archivo para que sirve, por que fue 
desarrollado y como probarlo.

Dentro de la carpeta que usted creo se encuentran dos carpetas mas: 
1) Entrega1_Medinilla (Proyecto)
2) WebF1 (Aplicacion)

Dentro de la primera carpeta (Entrega1_Medinilla) se creo el proyecto de esta carpeta los dos archivos que nos importan son 
urls.py y settings.py. En el archivo urls.py al abrirlo se encontrara con un diccionario "urlpatterns", donde se encuentran
la direccion que lo redirige al sitio de administracion de usuarios de django y un url con argunmento vacio ('') que vincula todos 
los urls utilizados en la aplicacion 'WebF1' con el proyecto actual. El hecho de que este vacio nos permite que usted con 
solo hacer click ingrese a los urls de la aplicacion. 
Si desea ingresar al administrador de Django en el link provisto por el terminal escriba '/admin/'.

El archivo settings.py contiene las configuraciones del proyecto, nos centraremos en 2:
INSTALLED_APPS, un diccionario que contiene todas las aplicaciones instaladas en el proyecto, al final del diccionario podra notar
que dice 'WebF1', nuestra aplicacion esta instalada en el proyecto.
TEMPLATES y dentro de dicho diccionario buscamos DIRS, esa ruta relativa es la que le indica al proyecto en que lugar buscar los 
templates al momento de llamarlos con las funciones. 

Ahora pasaremos a la siguiente carpeta 'WebF1', en esta carpeta se inicio la aplicacion, y dentro de ella esta todo lo referido 
a la misma. Iremos describiendo cada archivo que hay en la misma.

Archivo 'models.py'

En este archivo se desarrollaron cada uno de los modelos que nos interesaba tener en nuestra aplicacion, los cuales son:
Team, Empleados, de la cual heredan los modelos Ingeniero y Piloto, y dos modelos independientes llamados Fans y periodistas.
Dentro de cada modelo se definen campos de datos tales como nombre, apellido, edad, etc. Cada campo se ve reflejado en 
la base de datos. La forma de saber si esto funciona es al fijarnos en la base de datos, si tenemos los modelos creados en la 
misma entonces esta bien. 

Archivo 'forms.py' 

En este archivo se toman como base los modelos ya creados y mediante la funcion forms.form creamos el codigo que la aplicacion 
necesita para posteriormente poder desarrollar un API form y que el usuario pueda registrarse y sus datos queden guardados en la
base de datos. Notese que las variables dentro de cada clase son las mismas que en el archivo 'models.py', esto es asi para que cada
dato se guarde donde corresponde. 
La forma de saber que funciona sera mediante las funciones desarrolladas en el views.py, si los datos ingresados son reflejados 
en la BD entonces vamos bien.

Archivo 'views.py'

En el presente archivo se desarrollan las funcionalidades que vamos a necesitar. La primera funcion definida es 'Inicio' esta no hace 
mas que cargar el html de la pagina de inicio cuando usted ingresa al link. Si al clickear en el link se cargo una pagina de inicio
con lo antes descripto entonces esta funcion esta funcionando correctamente.

La siguiente funcion definida es 'Escuderias', la tarea de esta es tanto cargar el template correspondiente a la misma como cargar 
el formulario de carga de datos del modelo Team para que los usuarios (escuderias) puedan registrarse en la pagina. 
La forma de probar esta funcion desde la pagina web son dos: La mas sencilla es desde la barra de navegacion arriba clickear en la seccion 
'Registrarse', al hacer click nos llevara a esta seccion y alli podremos elegir de que manera nos queremos registrar, en este caso hacemos 
click en 'Escuderias', esto nos redirigira a una nueva pagina donde habra un formulario de carga de datos para escuderias. Si ingresamos
los datos, los enviamos y estos se ven reflejados en la BD entonces tanto la funcion como los formularios, y modelos funcionan de manera
correcta.
Las siguientes funciones 'Pilotos','Ingenieros','Fans' y 'Periodistas' realizan exactamente la misma tarea que la funcion antes descripta
solo que plasman sus datos en la BD correspondiente a cada modelo. 

Debajo de estas funciones hay dos mas, definidas como 'Busqueda' y 'Buscar'. La primera no hace mas que cargar el template correspondiente, 
pero la segunda nos permite mediante un nombre encontrar aquellos datos que necesitamos y mostrarlos en un template correspondiente 
de manera ordenada. 

Archivo 'urlsApp.py'

Este archivo es similar al que esta en el proyecto, posee un diccionario urlpatterns en el cual se encuentran las rutas a cada una de
las funciones del archivo views.py. 

Carpeta 'static' 

Dentro de esta carpeta se encuentran cada uno de los templates que se utilizaron en la aplicacion. Para el desarrollo de esta 
pagina web descargamos un template ya armado con su codigo html y su css y java correspondiente, no nos centraremos mucho en eso.

El template mas importante es "Padre.html" por que todos los demas heredan de este, y las modificaciones realizadas son en 
apenas algunas secciones de interes. 

"Inicio.html" es el que posee la estructura html de la pagina de inicio. La forma de probarla es ingresando al link provisto por el
terminal. Si cargo la pagina de inicio con toda la info de la Formula 1, entonces este template, la funcion asociada y el template
padre funcionan correctamente.

'Escud.html' este archivo posee la estructura de la pagina de registro de las escuderias, con el API form correspondiente. Aqui
podra registrarse como escuderia completando los campos solicitados. Para pobrar este template y la funcion asociada ingrese al
siguiente link: 'http://127.0.0.1:8000/Escuderias/'. Si se cargo lo antes descripto entonces anda correctamente. 

Todos los htmls, a excepcion de 'Busqueda.html' y 'Resultados.html' que describiremos a la brevedad, cumplen funciones similares,
por lo que para no extendernos de mas simplemente dejaremos los links para probarlos.

'Fans.html' : 'http://127.0.0.1:8000/Fans/'
'Ingenieros.html': http://127.0.0.1:8000/Ingenieros/
'Periodistas.html':http://127.0.0.1:8000/Periodistas/
'Piloto.html': http://127.0.0.1:8000/Pilotos/

El archivo 'Busqueda.html' contiene la estructura de la pagina donde podremos realizar la busqueda de datos guardados en nuestra BD.
Posee el form necesario para poder buscar y se conecta con la funcion buscar del archivo views.py. El link para probarlo es:
http://127.0.0.1:8000/Busqueda 

El archivo 'Resultados.html' contiene la estructura de la pagina donde se veran reflejados los resultados de la busqueda que hemos 
realizado con anterioridad. Nosotros hemos precargado algunos datos en nuestra base de datos a fin de verificar que todo el codigo
funciona de manera correcta y ahora haremos uso de estos para verificar la funcionalidad. 
Hemos cargado 1 objeto de cada modelo, por lo que al buscar deberan aparecer los datos simplemente de ese objeto. Se muestran datos
de una clase llamada empleados, de la cual, como explicamos antes, heredan los modelos piloto e ingeniero, por lo que los datos reflejados
en este apartado seran tanto de los objetos piloto como ingeniero. A continuacion los links para probar que la busqueda en la base 
de datos y todas las funcionalidades necesarios funcionan de manera correcta:

Objeto Team: 'http://127.0.0.1:8000/Buscar/?buscar=Mercedes+Benz'

Objeto Piloto: 'http://127.0.0.1:8000/Buscar/?buscar=Fernando'

Objeto Ingeniero: 'http://127.0.0.1:8000/Buscar/?buscar=Raul'

Objeto Fan: 'http://127.0.0.1:8000/Buscar/?buscar=Minguito'

Objeto Periodista: 'http://127.0.0.1:8000/Buscar/?buscar=Pepe'

Si en algun momento se carga algun otro objeto en la base de datos, para poder buscarlo, como aclara en la pagina de busqueda, simplemente
se debe introducir el nombre, y en la pagina resultados se veran reflejados todos los objetos de cada clase que contengan ese nombre. 

Si al seguir cada paso listado hasta aqui la pagina respondio de manera correcta entonces quiere decir que el codigo funciona de la forma que 
esperabamos. 
-----------------------------------------------------------------------------------------------------------------

COMO ARMAMOS EL PROYECTO 

Si leyo la seccion anterior se podra dar cuenta que el orden en el cual estan descripto cada uno de los archivos, y funcionalidades 
no es aleatorio, sino que este es el orden que nosotros seguimos para armar nuestro proyecto. 
Primero se crearon los modelos, luego las formas, luego las funciones para cargar los datos de dichos modelos, luego los templates
necesarios para que el usuario pueda interactuar y registrarse y luego las funciones de busqueda en la base de datos para poder 
acceder a los datos ya registrados, y por ultimo los templates para que el usuario pueda buscar. 







