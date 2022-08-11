ENTREGA DEL PROYECTO FINAL
Plataforma: Coderhouse

Grupo conformado por:
- Sergio Andrade
- Tomas Ruiz
- Tadeo Medinilla

Antes de comenzar con el desarrollo de este archivo los invitamos a acceder al siguiente link donde encontraran una pequeña
introduccion audiovisual al proyecto que desarrollamos. 
Link al video de presentacion: ' https://drive.google.com/file/d/1ZqyH5i9KlsVTbbwbwjB05Idfyat0TSJ9/view?usp=sharing '

Tema: En el proyecto desarrollamos una pagina web sobre la F1 donde los usuarios pogran registrarse, mandar mensajes a
otros usuarios, leer y crear publicaciones. A su vez entidades como escuderias, ingenieros, pilotos, periodistas y Fans
podran inscribirse en una base de datos donde sus datos quedaran guardados y podran ser mostrados, modificados y eliminados.

Desarrollo: La metodologia que empleamos para el desarrollo de este proyecto fue realizar videollamadas y debatir las ideas 
que iban surgiendo y escribiendo el codigo todos juntos, esto nos permitio aclarar dudas que surgieron en el camino, y que 
todos tomaramos participacion en todos los estadios del proyecto, es por eso que se hace dificil definir de manera puntual
que hizo cada uno. 

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

A continuacion detallaremos lo que se encuentra en cada carpeta, lo que hay en cada archivo, para que sirve, por que fue 
desarrollado y como probarlo.

Dentro de la carpeta que usted creo se encuentran tres carpetas mas: 
1) Entrega1_Medinilla (Proyecto)
2) WebF1 (Aplicacion)
3) Mensajeria (Aplicacion)

Dentro de la primera carpeta (Entrega1_Medinilla) se creo el proyecto de esta carpeta los dos archivos que nos importan son 
urls.py y settings.py. En el archivo urls.py al abrirlo se encontrara con un diccionario "urlpatterns", donde se encuentran
la direccion que lo redirige al sitio de administracion de usuarios de django, un segundo url con argunmento vacio ('') que vincula 
todos los urls utilizados en la aplicacion 'WebF1' con el proyecto actual, y un tercer url con argumento vacio tambien ('') que 
vincula los urls utilizados en la aplicacion 'Mensajeria'. El hecho de que este vacio nos permite que usted con solo hacer click
ingrese a los urls de la aplicacion. Si desea ingresar al administrador de Django en el link provisto por el terminal escriba 
'/admin/'.

El archivo settings.py contiene las configuraciones del proyecto, nos centraremos en 2:
 - INSTALLED_APPS, un diccionario que contiene todas las aplicaciones instaladas en el proyecto, al final del diccionario podra notar
que dice 'WebF1' y 'Mensajeria', nuestras aplicaciones estan instaladas en el proyecto.
 - TEMPLATES y dentro de dicho diccionario buscamos DIRS, esa ruta relativa es la que le indica al proyecto en que lugar buscar los 
templates al momento de llamarlos con las funciones. 

Ahora pasaremos a la siguiente carpeta 'WebF1', en esta carpeta se inicio la aplicacion, y dentro de ella esta todo lo referido 
a la misma. Iremos describiendo cada archivo que hay en la misma.

 - Archivo 'models.py'

En este archivo se desarrollaron cada uno de los modelos que nos interesaba tener en nuestra aplicacion, los cuales son:
Team, Empleados, de la cual heredan los modelos Ingeniero y Piloto, y otros modelos independientes llamados Fans, Periodistas, 
Publicaciones, Creadores y Avatar, cabe aclarar que se importo el modelo User para crear los usuarios.
Dentro de cada modelo se definen campos de datos tales como nombre, apellido, edad, etc. Cada campo se ve reflejado en 
la base de datos. La forma de saber si esto funciona es al fijarnos en la base de datos, si tenemos los modelos creados en la 
misma entonces esta bien. 

 - Archivo 'forms.py' 

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

Se definen las funciones que nos serviran para buscar objetos en la base de datos, las mismas son:
- 'Busqueda': Esta no hace mas que cargar el template donde podremos ingresar los datos del objeto que queremos buscar. 
- 'Buscar': Esta funcion nos permite buscar entre los objetos de las clases Team, Ingeniero, Piloto, Fans y Periodistas y mostrar los
resultados ordenados en un template.

Posteriormente se encuentran las funciones que nos permiten interactuar en la Web en forma de usuario, a continuacion las enlistamos 
y aclaramos brevemente su funcionamiento.
- 'Register': Esta funcion nos permite crear un usuario y guardarlo para poder acceder a funciones como mandar mensajes o realizar
publicaciones.
- 'Login': Esta funcion nos permite, una vez creado el usuario, iniciar sesion.
- 'Logout': Esta funcion nos permite, una vez creado el usuario y con la sesion iniciada, cerrar sesion.
- 'ModificarUsuario': Esta funcion nos permite modificar los datos del usuario y guardarlos.
- 'DetalleUsuario': Esta funcion carga un template en el que se veran los datos detallados del usuario actual.
- 'AgregarAvatar': Esta funcion nos permitira agregarle una imagen a nuestro usuario.

A partir de aqui el documento contiene comentarios que lo dividen siempre igual, ya que lo que tenemos a continuacion 
son los CRUD's de cada clase. Un CRUD (Create, Read, Update, Delete) es una parte del codigo en la que se definen 
funciones, que como lo dicen sus siglas en ingles nos permiten crear, leer, modificar y eliminar un objeto de una clase. 
Procederemos a explicar como funciona el CRUD de la clase Team, y  solo este, debido a que luego se realiza exactamente 
lo mismo para las demas clases, por lo que se puede hacer extensiva esta explicacion para ellas. 

CRUD escuderias:
- Create = Funcion 'Escuderias': 
    En esta funcion lo que hacemos es crear un objeto de la clase team, para ello hacemos uso de un formulario creado 
    previamente para esta clase llamado 'TeamForm' que nos permitira llevar los datos ingresados en formulario a la BD 
    y guardarlos en los campos correspondientes del modelo Team. 
- Read = Funcion 'LeerEscuderias': 
    Aqui lo que hacemos es traer todos los objetos de esta clase creados y mostrarlos en forma de lista, para posteriormente
    poder modificarlos, eliminarlos o verlos en detalle. 
- Update = Funcion 'ModificarEscuderia':
    Esta funcion nos permite modificar un objeto en particular asignandole nuevos valores a los campos que ya teniamos 
    anteriormente. 
- Delete = Funcion 'EliminarEscuderia':
    Esta funcion elimina el objeto en particular que nosotros seleccionemos. 

Cabe aclarar que en cada division CRUD agregamos una ultima funcion, la cual nos permite ver un objeto seleccionado en detalle.
Esta funcion se llama, en el caso de escuderias 'DetalleEscuderia'.

Por ultimo en este archivo tenemos un apartado de publicaciones, este conjunto de funciones nos permite crear una nueva publicacion,
listar las publicaciones que ya hay realizadas, eliminar una publicacion y ver en detalle una publicacion en especifico.  

Nota: La funcion 'AboutUs' carga el template en el que se encuentran los datos de los creadores del sitio web.

Archivo 'urlsApp.py'

Este archivo es similar al que esta en el proyecto, posee un diccionario urlpatterns en el cual se encuentran las rutas a cada una de
las funciones del archivo views.py. Notese que la variable urlpatterns esta ordenada siguiendo la misma division de CRUDs que en el 
archivo views.py, esto permite rapidez en caso de querer corregir o modificar algo en el codigo. 

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
Hemos cargado 1 objeto de cada modelo, por lo que al buscar deberan aparecer los datos simplemente de ese objeto. A continuacion los
links para probar que la busqueda en la base de datos y todas las funcionalidades necesarios funcionan de manera correcta:

Objeto Team: 'http://127.0.0.1:8000/Buscar/?buscar=Mercedes+Benz'

Objeto Piloto: 'http://127.0.0.1:8000/Buscar/?buscar=Fernando'

Objeto Ingeniero: 'http://127.0.0.1:8000/Buscar/?buscar=Raul'

Objeto Fan: 'http://127.0.0.1:8000/Buscar/?buscar=Minguito'

Objeto Periodista: 'http://127.0.0.1:8000/Buscar/?buscar=Pepe'

Si en algun momento se carga algun otro objeto en la base de datos, para poder buscarlo, como aclara en la pagina de busqueda, 
simplemente se debe introducir el nombre, y en la pagina resultados se veran reflejados todos los objetos de cada clase que 
contengan ese nombre. 

Como explicamos con anterioridad a cada objeto se lo puede crear, leer, modificar y eliminar, esto se realiza en diferentes 
templates a continuacion enlistaremos los mismos para los objetos de la clase escuderia, al igual que antes, esta explicacion
se hace extensiva a todas las clases. 

Template para crear un objeto escuderia: 'Escud.html', en este template tenemos el formulario para la creacion de un objeto
    escuderia. Para probar este template ingrese a 'http://127.0.0.1:8000/Escuderias/', aqui va a encontrar un formulario de 
    inscripcion, si lo completa se realizara la inscripcion y lo enviara al inicio.
Template que muestra los objetos: 'MostrarEscuderias.html', en este template se enlistan todas las escuderias inscriptas en
    la pagina web. En caso de no haber inscriptos se mostrara un mensaje de que 'Aun no hay inscriptos'. 
    Para probar esto ingrese a 'http://127.0.0.1:8000/MostrarEscuderias/'.
Template que permite realiza modificaciones: 'ModificarEscuderia.html', aqui podremos modificar los datos de una escuderia en 
    particular y guardarlos. Para poder probar este template debe haber generado un objeto previamente, ya que por url hay 
    que pasarle un id de cada objeto. Sugerimos que desde la direccion de Mostrar escuderias seleccione un objeto y le de a 
    modificar esto lo redirigira al template descripto y podra modificar el objeto.
Template que muestra la info de un objeto: 'EscuderiaDetail.html' en este template mostramos la informacion ampliada de un 
    un objeto en particular. Para poder probar este template debe haber generado un objeto previamente, ya que por url hay 
    que pasarle un id de cada objeto. Sugerimos que desde la direccion de Mostrar escuderias seleccione un objeto y le de a 
    detalle esto lo redirigira al template descripto y podra ver la informacion ampliada del objeto.

No hay un template especifico para eliminar un objeto, esta accion se puede realizar desde los templates en donde se enlistan
todos los objetos, o desde el detalle de un objeto en particular, simplemente hay que clickear en el boton de eliminar objeto.

Si al seguir cada paso listado hasta aqui la pagina respondio de manera correcta entonces quiere decir que el codigo funciona 
de la forma que esperabamos. 

Para finalizar hablaremos de los archivos dentro de la carpeta 'Mensajeria' en la cual se desarrollo la aplicacion que permite 
a los usuarios enviar y recibir mensajes. 

Al igual que en la carpeta anterior los archivos 'modelsMensajeria.py', 'formsMensajeria.py' y 'urlsMensajeria.py' cumplen las mismas funciones, por 
lo que no nos extenderemos demasiado. En el archivo modelsMensajeria.py encontramos los modelos de datos que creemos necesarios para 
el desarrollo de la aplicacion, en el archivo 'formsMensajeria.py' se encuentran los formularios que nos permitiran guardar los
datos en los campos correspondientes a la hora de cargarlos desde la web, y en el urlsMensajeria.py se encuentran las direcciones
que relacionan las funciones con el url de la web. 

'viewsMensajeria.py' 

En este archivo desarrollamos las funciones necesarias para poder crear un mensaje nuevo, mostrar los mensajes que recibimos, 
responder los mensajes pendientes y eliminar los mensajes que no deseamos tener. 
A continuacion enlistamos las funciones y su comportamiento esperado:
    - 'Mensaje': Esta funcion nos permite que, con la sesion iniciada, los usuarios creen un nuevo mensaje y lo envien a otro 
    usuario registrado en la pagina. 
    - 'MostrarMensajes': Esta funcion permite que al ingresar a la seccion mensajes se enlisten todos los mensajes que hemos
    recibido. 
    - 'ResponderMensaje': Como su nombre lo indica con esta funcion realizamos la respuesta de un mensaje en particular.
    - 'EliminarMensaje': Nos permite eliminar un mensaje en particular. 

Se recomienda que para probar estas funcionalidades se creen dos usuarios, ingresando en uno de ellos se envie un mensaje al 
otro,  luego se inicie sesion con el otro usuario, vaya a la seccion mensajes y desde alli podra ver el mensaje, reponderlo
o eliminarlo segun desee. En caso de responderlo puede iniciar sesion nuevamente con el primer usuario, ingresar a la seccion 
mensajes y alli vera la respuesta. 


-----------------------------------------------------------------------------------------------------------------

COMO ARMAMOS EL PROYECTO 

Si leyo la seccion anterior se podra dar cuenta que el orden en el cual estan descripto cada uno de los archivos, y funcionalidades 
no es aleatorio, sino que este es el orden que nosotros seguimos para armar nuestro proyecto. 
Primero se crearon los modelos, luego las formas, luego las funciones para cargar los datos de dichos modelos, luego los templates
necesarios para que el usuario pueda interactuar y registrarse y luego las funciones de busqueda en la base de datos para poder 
acceder a los datos ya registrados, y por ultimo los templates para que el usuario pueda buscar. 

Asi concluye nuestro proyecto, muchas gracias por tomarse el tiempo de leer este archivo y de realizar la prueba de la pagina. 








