from django.shortcuts import render
from django.template import loader
from WebF1.forms import PilotoForm, TeamForm, IngenieroForm, PeriodistaForm, FanForm
from WebF1.models import Ingeniero, Periodista, Piloto, Team, Fan
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy




def Inicio(request):

    return render(request, 'Inicio.html' )


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
            return render(request, 'Inicio.html')
    else:
        MiForm = TeamForm()
        
    return render(request, 'Escud.html', {'MiForm': MiForm})
# Read:
def LeerEscuderias(request):

    escuderias = Team.objects.all()
    lista = {'escuderias': escuderias}
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
            lista = {'escuderias':escuderias}
            
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
    
    return render(request,'ModificarEscuderia.html/', {'MiForm': MiForm, 'escuderia': pk} )
# Delete:
def EliminarEscuderia(request, pk):
    
    team = Team.objects.get(pk = pk)
    team.delete()

    escuderias = Team.objects.all()
    lista = {'escuderias':escuderias}

    return render(request,'MostrarEscuderias.html/', lista )

#Detail [No es parte del CRUD lo utilizo para mostrar info detallada de un objeto en especifico]:
class DetalleEscuderia(DetailView):
    
    model = Team
    template_name = 'EscuderiaDetail.html'

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
            return render(request, 'Inicio.html')
    else:
        MiForm = PilotoForm()
        
    return render(request, 'Piloto.html', {'MiForm': MiForm})
# Read:
def LeerPilotos(request):
    
    pilotos = Piloto.objects.all()
    lista = {'pilotos': pilotos}

    return render(request, 'MostrarPilotos.html/', lista)
#Update
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
            lista = {'pilotos':pilotos}
            
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
    
    return render(request,'ModificarPiloto.html/', {'MiForm': MiForm, 'piloto': pk} )
#Delete
def EliminarPiloto(request, pk):
       
    piloto = Piloto.objects.get(pk = pk)
    piloto.delete()

    pilotos = Piloto.objects.all()
    lista = {'pilotos':pilotos}

    return render(request,'MostrarPilotos.html/', lista )

#Detail [No es parte del CRUD lo utilizo para mostrar info detallada de un objeto en especifico]:
class DetallePiloto(DetailView):
    
    model = Piloto
    template_name = 'PilotoDetail.html'

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
            return render(request, 'Inicio.html')
    else:
        MiForm = IngenieroForm()
        
    return render(request, 'Ingenieros.html', {'MiForm': MiForm})
#Read:
def LeerIngenieros(request):

    ingenieros = Ingeniero.objects.all()
    lista = {'ingenieros':ingenieros}
    
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
           
            ingenieros = Ingeniero.objects.all()
            lista = {'ingenieros':ingenieros}
            
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
    
    return render(request,'ModificarIngeniero.html/', {'MiForm': MiForm, 'ingeniero': pk} )
#Delete:
def EliminarIngeniero(request, pk):
    #NOTA: Trabajo con el pk y no con el nombre registrado por que si hay dos objetos con el mismo nombre
    # el codigo no sabe cual llamar, el pk es unico para cada objeto.

    ingeniero = Ingeniero.objects.get( pk = pk)
    ingeniero.delete()

    ingenieros = Ingeniero.objects.all()
    lista = {'ingenieros':ingenieros}

    return  render(request, 'MostrarIngenieros.html/', lista)

#Detail [No es parte del CRUD lo utilizo para mostrar info detallada de un objeto en especifico]:
class DetalleIngeniero(DetailView):
    
    model = Ingeniero
    template_name = 'IngenieroDetail.html'

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
