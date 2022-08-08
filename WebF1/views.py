from pickle import FALSE, TRUE
from django.shortcuts import render
from django.template import loader
from WebF1.forms import PilotoForm, PublicacionForm, TeamForm, IngenieroForm, PeriodistaForm, FanForm, UserRegisterForm, UserEditForm, AvatarForm
from WebF1.models import Creador, Ingeniero, Periodista, Piloto, Publicaciones, Team, Fan, Avatar
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date



def Inicio(request):

    return render(request, 'Inicio.html' )

def AboutUs(request):

    tomas = Creador(nombre='Tomas', apellido='Ruiz', descripcion='tomas descripcion')
    sergio = Creador(nombre='Sergio', apellido='Andrade', descripcion='sergio descripcion')
    tadeo = Creador(nombre='Tadeo', apellido='Medinilla', descripcion='tadeo descripcion')
    notificacion = 'Aquí conoceras mas sobre nosotros.'
    modelo={'tomas': tomas, 'sergio':sergio,'tadeo':tadeo, 'notificacion':notificacion}

    return render(request, 'AboutUs.html', modelo )

#Funciones necesarias para la busqueda en la BD:
def Busqueda(request):
    
    return render(request, 'Busqueda.html/')

def Buscar(request):
    
    
    if request.GET['buscar']:
        search= request.GET['buscar']
        #Busco dentro del model Team:
        team= Team.objects.filter(escuderia=search)
        #Busco dentro del model ingeniero
        ingeniero = Ingeniero.objects.filter(nombre = search)
        #Busco dentro del model piloto
        piloto = Piloto.objects.filter(nombre = search)
        #Busco dentro del model fans
        fan = Fan.objects.filter(nombre = search)
        #Busco dentro del model periodista
        periodista = Periodista.objects.filter(nombre = search)
        

        return render(request,'Resultados.html/', {"teams":team,
                                                    "ingenieros":ingeniero,
                                                    "pilotos":piloto,
                                                    "Fans":fan,
                                                    "periodistas":periodista} )
    else:
        return render(request, 'Busqueda.html/', {"error": 'No hay datos'})

#Inicio de sesion:
def Login(request):
    if request.method == 'POST':
        MiForm = AuthenticationForm(request, data = request.POST)

        if MiForm.is_valid():

            usuario = MiForm.cleaned_data.get('username')
            contrasena = MiForm.cleaned_data.get('password')

            user = authenticate(username= usuario, password = contrasena)

            if user is not None:
                login(request, user)
                return render(request, 'Inicio.html', {'Notificacion': f'Bienvenido {usuario}'})
            
            else: 
                return render(request, 'Inicio.html', {'Notificacion': 'Error, datos incorrectos'})
            
        else:
            return render(request, 'Inicio.html', {'Notificacion' : 'Error, formulario incorrecto'})
    
    MiForm = AuthenticationForm

    return render(request, 'Login.html',  {'MiForm': MiForm})
#Registrarse:
def Register(request):
    
    if request.method == 'POST':

        MiForm = UserRegisterForm(request.POST)

        if MiForm.is_valid():

            username = MiForm.cleaned_data['username']
            MiForm.save()

            return render(request, 'Inicio.html', {'Notificacion': 'Usuario creado'})
    else:
        MiForm = UserRegisterForm()
    
    return render(request, 'Register.html', {'MiForm': MiForm})

def ModificarUsuario(request,pk):

    u = User.objects.get(pk=pk)

    if request.method == 'POST':
        MiForm = UserEditForm(request.POST)
        print(MiForm)
        if MiForm.is_valid:

            info = MiForm.cleaned_data

            #u.user = info['username']
            u.first_name = info['first_name']
            u.last_name = info['last_name']
            u.email = info['email']
            u.password1 = info['password1']
            #u.password2 = info['password2']

            u.save()

            return render(request, 'Inicio.html')
    
    else:
        MiForm = UserEditForm(initial = {'username': u.username, 
                                        'first_name': u.first_name,
                                        'last_name':u.last_name,
                                        'email':u.email
                                        })

    return render(request, 'ModificarUsuario.html', {'MiForm': MiForm })
#Detail:
class DetalleUsuario(DetailView):
    
    model = User
    template_name = 'UserDetail.html'

def AgregarAvatar(request):

    if request.method == 'POST':
        MiForm = AvatarForm(request.POST, request.FILES)
        if MiForm.is_valid:
            avatarViejo=Avatar.objects.get(user = request.user)
            if(avatarViejo.imagen):
                avatarViejo.delete()
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=MiForm.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'Inicio.html')
    else:
        MiForm = AvatarForm()
    return render(request, 'AgregarAvatar.html', {'MiForm': MiForm, 'user': request.user})

listo = TRUE
#C.R.U.D. [Create, Read, Update, Delete] de Escuderias:
#Create:
def Escuderias(request):
#En este template voy a tener info ampliada sobre las escuderias y un API form.
    if request.method == 'POST':
       
        MiForm = TeamForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:

            info = MiForm.cleaned_data
            escuderia= Team( escuderia = info['escuderia'],
                        nacionalidad = info['nacionalidad'],
                        patrocinador = info ['patrocinador'],
                        proov_motor = info['proovedor_motor'],
                        mod_motor = info['modelo_del_motor'],
                        proov_chasis = info['proovedor_chasis'],
                        mod_chasis = info['modelo_chasis'],
                        gp_anfitrion = info['gp_anfitrion'],
                        pil_ppal = info['piloto_principal'],
                        pil_sec = info['piloto_secundario'],
                        cant_emp = info['cantidad_de_empleados'])
            escuderia.save()
            
            notificacion='Te has inscripto como escuderia.\nVe a la seccion escuderias para ver tus datos'
            modelo={'notificacion':notificacion}
            
            return render(request, 'Inicio.html',modelo)
    else:
        MiForm = TeamForm()
        notificacion='Aqui te podras inscribir como escuderia'
    return render(request, 'Escud.html', {'MiForm': MiForm,'notificacion':notificacion})
# Read:
def LeerEscuderias(request):

    escuderias = Team.objects.all()
    notificacion='Aqui se listan todas las escuderias'
    lista = {'escuderias': escuderias,'notificacion':notificacion}

    return render(request, 'MostrarEscuderias.html/', lista )
# Update:
def ModificarEscuderia(request, pk):

    escuderia = Team.objects.get(pk = pk)

    if request.method == 'POST':
       
        MiForm = TeamForm(request.POST)
        print(MiForm)
        if MiForm.is_valid:
            info = MiForm.cleaned_data
            
            escuderia.escuderia=info['escuderia']
            escuderia.nacionalidad= info['nacionalidad']
            escuderia.patrocinador=info ['patrocinador']
            escuderia.proov_motor=info['proovedor_motor']
            escuderia.mod_motor=info['modelo_del_motor']
            escuderia.proov_chasis=info['proovedor_chasis']
            escuderia.mod_chasis=info['modelo_chasis']
            escuderia.gp_anfitrion= info['gp_anfitrion']
            escuderia.pil_ppal=info['piloto_principal']
            escuderia.pil_sec=info['piloto_secundario']
            escuderia.cant_emp=info['cantidad_de_empleados']
            
            escuderia.save()
            
            escuderias = Team.objects.all()
            notificacion='Modificacion guardada.'
            lista = {'escuderias':escuderias, 'notificacion':notificacion}
            
            
            return render(request, 'MostrarEscuderias.html/', lista)
    else:
        MiForm = TeamForm(initial={'escuderia': escuderia.escuderia,
                         'nacionalidad': escuderia.nacionalidad, 
                         'patrocinador': escuderia.patrocinador,
                         'proovedor_motor':escuderia.proov_motor,
                         'modelo_del_motor':escuderia.mod_motor,
                         'proovedor_chases':escuderia.proov_chasis,
                         'modelo_chasis':escuderia.mod_chasis,
                         'gp_anfitrion':escuderia.gp_anfitrion,
                         'piloto_principal':escuderia.pil_ppal,
                         'piloto_secundario':escuderia.pil_sec,
                         'empleados':escuderia.cant_emp})
        notificacion='Aqui podras modificar tus datos de escuderia.'
        
    
    return render(request,'ModificarEscuderia.html/', {'MiForm': MiForm, 'escuderia': pk, 'notificacion':notificacion} )
# Delete:
def EliminarEscuderia(request, pk):
    
    team = Team.objects.get(pk = pk)
    team.delete()

    escuderias = Team.objects.all()
    notificacion='Escuderia eliminada.'
    lista = {'escuderias':escuderias,'notificacion':notificacion}

    return render(request,'MostrarEscuderias.html/', lista )

#Detail [No es parte del CRUD lo utilizo para mostrar info detallada de un objeto en especifico]:
class DetalleEscuderia(DetailView):
    
    model = Team
    template_name = 'EscuderiaDetail.html'

listo = TRUE
#C.R.U.D. [Create, Read, Update, Delete] de Pilotos:
#Create:
def Pilotos(request):
#En este template voy a tener info ampliada sobre los pilotos y un API form.
    if request.method == 'POST':
       
        MiForm = PilotoForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:

            info = MiForm.cleaned_data
            piloto = Piloto (                        
                        nombre = info['nombre'],
                        apellido=info['apellido'],
                        nacionalidad = info['nacionalidad'],
                        experiencia=info['experiencia'],
                        edad=info['edad'],
                        escuderia = info['escuderia'],
                        puesto=info['puesto'],
                        campeonatos_disputados= info['campeonatos_disputados'],
                        campeonatos_ganados=info['campeonatos_ganados'],
                        circuito_favorito=info['circuito_favorito'],
                        poles= info['poles'],
                        carreras_disputadas= info['carreras_disputadas'],
                        carreras_ganadas=info['carreras_ganadas'],
                        email=info['email'])
                        
            piloto.save()

            notificacion='Te has inscripto como piloto.\nVe a la seccion pilotos para ver tus datos'
            modelo={'notificacion':notificacion}

            return render(request, 'Inicio.html', modelo)
    else:
        MiForm = PilotoForm()
        notificacion='Aqui te podras inscribir como escuderia'
    return render(request, 'Piloto.html', {'MiForm': MiForm,'notificacion':notificacion })
# Read:
def LeerPilotos(request):
    
    pilotos = Piloto.objects.all()
    notificacion='Aqui se listan todos los pilotos'
    lista = {'pilotos': pilotos, 'notificacion':notificacion}

    return render(request, 'MostrarPilotos.html/', lista)
#Update:
def ModificarPiloto(request, pk):

    piloto = Piloto.objects.get(pk = pk)

    if request.method == 'POST':
       
        MiForm = PilotoForm(request.POST)
        print(MiForm)
        if MiForm.is_valid:

            info = MiForm.cleaned_data
            
            piloto.nombre=info['nombre']
            piloto.apellido=info['apellido']
            piloto.nacionalidad=info['nacionalidad']
            piloto.experiencia=info['experiencia']
            piloto.edad=info['edad']
            piloto.escuderia=info['escuderia']
            piloto.puesto=info['puesto']
            piloto.campeonatos_disputados=info['campeonatos_disputados']
            piloto.campeonatos_ganados=info['campeonatos_ganados']
            piloto.circuito_favorito=info['circuito_favorito']
            piloto.poles=info['poles']
            piloto.carreras_disputadas=info['carreras_disputadas']
            piloto.carreras_ganadas=info['carreras_ganadas']
            piloto.email=info['email']

            piloto.save()
           
            pilotos = Piloto.objects.all()
            notificacion='Modificacion guardada.'
            lista = {'pilotos':pilotos, 'notificacion':notificacion}
            
            return render(request, 'MostrarPilotos.html/', lista)
            
    else:
        MiForm = PilotoForm(initial= {'nombre': piloto.nombre,
                                     'apellido': piloto.apellido,
                                     'nacionalidad': piloto.nacionalidad, 
                                     'experiencia':piloto.experiencia,
                                     'edad':piloto.edad, 
                                     'escuderia':piloto.escuderia,
                                     'puesto':piloto.puesto,
                                     'campeonatos_disputados':piloto.campeonatos_disputados,
                                     'campeonatos_ganados':piloto.campeonatos_ganados,
                                     'carreras_disputadas':piloto.carreras_disputadas,
                                     'carreras_ganadas':piloto.carreras_ganadas,
                                     'poles':piloto.poles,
                                     'circuito_favorito':piloto.circuito_favorito,
                                     'email':piloto.email,})
        notificacion='Aqui podras modificar tus datos de piloto.'
    return render(request,'ModificarPiloto.html/', {'MiForm': MiForm, 'piloto': pk, 'notificacion':notificacion} )
#Delete:
def EliminarPiloto(request, pk):
       
    piloto = Piloto.objects.get(pk = pk)
    piloto.delete()

    pilotos = Piloto.objects.all()
    notificacion='Piloto eliminado.'
    lista = {'pilotos':pilotos,'notificacion':notificacion}

    return render(request,'MostrarPilotos.html/', lista )

#Detail [No es parte del CRUD lo utilizo para mostrar info detallada de un objeto en especifico]:
class DetallePiloto(DetailView):
    
    model = Piloto
    template_name = 'PilotoDetail.html'


listo = TRUE
#C.R.U.D. [Create, Read, Update, Delete] de Ingenieros:
#Create:
def Ingenieros(request):
#En este template voy a tener info ampliada sobre los Ing. y un API form.
    if request.method == 'POST':
       
        MiForm = IngenieroForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:
            
            info = MiForm.cleaned_data
            ingeniero = Ingeniero (nombre = info['nombre'],
                        apellido=info['apellido'],
                        nacionalidad = info['nacionalidad'],
                        experiencia=info['experiencia'],
                        edad=info['edad'],
                        escuderia = info['escuderia'],
                        puesto=info['puesto'],
                        universidad= info['universidad'],
                        titulo = info['titulo'],
                        especialidad = info['especialidad'],
                        ocupacion = info ['ocupacion'],
                        email = info['email'])

            ingeniero.save()

            notificacion='Te has inscripto como ingeniero.\nVe a la seccion ingenieros para ver tus datos'
            modelo={'notificacion':notificacion}

            return render(request, 'Inicio.html', modelo)
    else:
        MiForm = IngenieroForm()
        notificacion='Aqui te podras inscribir como ingeniero'
    return render(request, 'Ingenieros.html', {'MiForm': MiForm,'notificacion':notificacion})
#Read:
def LeerIngenieros(request):

    ingenieros = Ingeniero.objects.all()
    notificacion='Aqui se listan todos los ingenieros'
    lista = {'ingenieros':ingenieros,'notificacion':notificacion}
    
    return render(request, 'MostrarIngenieros.html/', lista)
#Update:
def ModificarIngeniero(request, pk):
    #NOTA: Trabajo con el pk y no con el nombre registrado por que si hay dos objetos con el mismo nombre
    # el codigo no sabe cual llamar, el pk es unico para cada objeto.
    
    ingeniero = Ingeniero.objects.get(pk = pk)

    if request.method == 'POST':
       
        MiForm = IngenieroForm(request.POST)
        print(MiForm)
        if MiForm.is_valid:

            info = MiForm.cleaned_data
            
            ingeniero.nombre=info['nombre']
            ingeniero.apellido=info['apellido']
            ingeniero.nacionalidad=info['nacionalidad']
            ingeniero.experiencia=info['experiencia']
            ingeniero.edad=info['edad']
            ingeniero.escuderia=info['escuderia']
            ingeniero.puesto=info['puesto']
            ingeniero.universidad=info['universidad']
            ingeniero.titulo=info['titulo']
            ingeniero.especialidad=info['especialidad']
            ingeniero.ocupacion=info['ocupacion']
            ingeniero.email=info['email']

            ingeniero.save()
            notificacion='Modificacion guardada.'
            ingenieros = Ingeniero.objects.all()
            lista = {'ingenieros':ingenieros, 'notificacion':notificacion}
            
            return render(request, 'MostrarIngenieros.html/', lista)
            
    else:
        MiForm = IngenieroForm(initial= {'nombre': ingeniero.nombre,
                                     'apellido': ingeniero.apellido,
                                     'nacionalidad': ingeniero.nacionalidad, 
                                     'experiencia':ingeniero.experiencia,
                                     'edad':ingeniero.edad, 
                                     'escuderia':ingeniero.escuderia,
                                     'puesto':ingeniero.puesto,
                                     'universidad':ingeniero.universidad,
                                     'titulo':ingeniero.titulo,
                                     'especialidad':ingeniero.especialidad,
                                     'ocupacion':ingeniero.ocupacion,
                                     'email':ingeniero.email,})
        notificacion='Aqui podras modificar tus datos de ingeniero.'
    return render(request,'ModificarIngeniero.html/', {'MiForm': MiForm, 'ingeniero': pk,'notificacion':notificacion } )
#Delete:
def EliminarIngeniero(request, pk):
    #NOTA: Trabajo con el pk y no con el nombre registrado por que si hay dos objetos con el mismo nombre
    # el codigo no sabe cual llamar, el pk es unico para cada objeto.

    ingeniero = Ingeniero.objects.get( pk = pk)
    ingeniero.delete()

    ingenieros = Ingeniero.objects.all()
    notificacion='Ingeniero eliminado.'
    lista = {'ingenieros':ingenieros,'notificacion':notificacion }

    return  render(request, 'MostrarIngenieros.html/', lista)

#Detail [No es parte del CRUD lo utilizo para mostrar info detallada de un objeto en especifico]:
class DetalleIngeniero(DetailView):
    
    model = Ingeniero
    template_name = 'IngenieroDetail.html'


listo = TRUE
#C.R.U.D. [Create, Read, Update, Delete] de Fans:
#Create:
class Fans(CreateView):

    model = Fan
    template_name = 'Fans.html'
    success_url = reverse_lazy( 'MostrarFans' )
    fields = [ 'nombre', 'apellido', 'email', 'edad' ]
#Read:
class MostrarFans(ListView):

    model = Fan
    template_name = 'MostrarFans.html'
#Update:
class ModificarFan(UpdateView):
    
    model = Fan
    template_name = 'Fans.html'
    success_url = reverse_lazy( 'MostrarFans' )
    fields = [ 'nombre', 'apellido', 'email', 'edad' ]
#Delete:
class EliminarFan(DeleteView):
    
    model = Fan
    template_name = 'EliminarFan_confirm.html'
    success_url = reverse_lazy( 'MostrarFans' )

#Detail [No es parte del CRUD lo utilizo para mostrar info detallada de un objeto en especifico]:
class DetalleFan(DetailView):
    
    model = Fan
    template_name = 'FanDetail.html'


listo = TRUE
#C.R.U.D. [Create, Read, Update, Delete] de Fans:
#Create:
class Periodistas(CreateView):

    model = Periodista
    template_name = 'Periodistas.html'
    success_url = reverse_lazy( 'MostrarPeriodistas' )
    fields = [ 'nombre', 'apellido', 'medio', 'matricula', 'email' ]
#Read:
class MostrarPeriodistas(ListView):

    model = Periodista
    template_name = 'MostrarPeriodistas.html'    
#Update:
class ModificarPeriodista(UpdateView):

    model = Periodista
    template_name = 'Periodistas.html'
    success_url = reverse_lazy( 'MostrarPeriodistas')
    fields = [ 'nombre', 'apellido', 'medio', 'matricula', 'email' ]
#Delete:
class EliminarPeriodista(DeleteView):

    model = Periodista
    template_name = 'EliminarPeriodista_confirm.html'
    success_url = reverse_lazy( 'MostrarPeriodistas')

#Detail [No es parte del CRUD lo utilizo para mostrar info detallada de un objeto en especifico]:
class DetallePeriodista(DetailView):
    
    model = Periodista
    template_name = 'PeriodistaDetail.html'


listo = TRUE
#CRUD Publicaciones:
#Create:
def Publicacion(request):
    if request.method == 'POST':

        MiForm = PublicacionForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:

            info = MiForm.cleaned_data
            publicacion = Publicaciones( autor = info['autor'], titulo = info['titulo'], cuerpo = info['cuerpo'], fecha = date.today() )
            
            publicacion.save()

            notificacion = 'Tu publicacion ha sido realizada. Ve a publicaciones para verla.'
            lista={'notificacion': notificacion}
            
            return render(request, 'Inicio.html', lista)
    else:
        MiForm = PublicacionForm()
    
    return render (request, 'Publicacion.html', {'MiForm': MiForm})                            
#Read:
def MostrarPublicaciones(request):

    publicaciones = Publicaciones.objects.all()
    lista = {'pubs':publicaciones}
    
    return render(request, 'MostrarPublicaciones.html/', lista)
#Delete:
class EliminarPublicacion(DeleteView):

    model = Publicaciones
    template_name = 'EliminarPublicacion_confirm.html'
    success_url = reverse_lazy( 'MostrarPublicaciones')
#Detail [No es parte del CRUD lo utilizo para mostrar info detallada de un objeto en especifico]:
class DetallePublicacion(DetailView):
       
    model = Publicaciones
    template_name = 'PublicacionDetail.html'

