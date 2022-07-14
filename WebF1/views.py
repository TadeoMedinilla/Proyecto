from django.shortcuts import render
from django.template import loader
from WebF1.forms import PeriodistaForm,FanForm, TeamForm, PilotoForm,IngenieroForm
from WebF1.models import Empleado, Ingeniero, Periodista, Piloto, Team, Fan
from django.http import HttpResponse
# Funciones necesarias para carga de templates y formularios de carga de datos
def Inicio(request):

    return render(request, 'Inicio.html' )

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

def Pilotos(request):
#En este template voy a tener info ampliada sobre los pilotos y un API form.
    if request.method == 'POST':
       
        MiForm = PilotoForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:

            info = MiForm.cleaned_data
            piloto = Piloto ( escuderia = info['escuderia'],
                        nacionalidad = info['nacionalidad'],
                        patrocinador = info ['patrocinador'],
                        nombre = info['nombre'],
                        apellido=info['apellido'],
                        edad=info['edad'],
                        puesto=info['puesto'],
                        exp=info['experiencia'],
                        camp_disp= info['campeonatos_disputados'],
                        camp_gan=info['campeonatos_ganados'],
                        circuito=info['circuito_favorito'])
            piloto.save()
            return render(request, 'Inicio.html')
    else:
        MiForm = PilotoForm()
        
    return render(request, 'Piloto.html', {'MiForm': MiForm})

def Ingenieros(request):
#En este template voy a tener info ampliada sobre los Ing. y un API form.
    if request.method == 'POST':
       
        MiForm = IngenieroForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:

            info = MiForm.cleaned_data
            ingeniero = Ingeniero ( escuderia = info['escuderia'],
                        nacionalidad = info['nacionalidad'],
                        nombre = info['nombre'],
                        apellido=info['apellido'],
                        edad=info['edad'],
                        puesto=info['puesto'],
                        exp=info['experiencia'],
                        universidad= info['universidad'],
                        titulo = info['titulo'],
                        especialidad = info['especialidad'],
                        email = info['email'])
            ingeniero.save()
            return render(request, 'Inicio.html')
    else:
        MiForm = IngenieroForm()
        
    return render(request, 'Ingenieros.html', {'MiForm': MiForm})

def Fans(request):
    #En este template voy a tener un API form.
    if request.method == 'POST':
       
        MiForm = FanForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:

            info = MiForm.cleaned_data
            fan =  Fan ( nombre = info['nombre'],
                        apellido=info['apellido'],
                        edad=info['edad'],
                        email=info['email'])
            fan.save()
            return render(request, 'Inicio.html')
    else:
        MiForm = FanForm()
        
    return render(request, 'Fans.html', {'MiForm': MiForm})

def Periodistas(request):
    #En este template voy a tener un API form.
    if request.method == 'POST':
       
        MiForm = PeriodistaForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:

            info = MiForm.cleaned_data
            periodista =  Periodista ( nombre = info['nombre'],
                        apellido=info['apellido'],
                        medio=info['medio'],
                        matricula=info['matricula'],
                        email=info['email'])
            periodista.save()
            return render(request, 'Inicio.html')
    else:
        MiForm = PeriodistaForm()
        
    return render(request, 'Periodistas.html', {'MiForm': MiForm})

#A partir de aca estan las funciones necesarias para la busqueda en la BD

def Busqueda(request):
    
    return render(request, 'Busqueda.html/')

def Buscar(request):
    
    #respuesta = "Estoy buscando"
    if request.GET['buscar']:
        search= request.GET['buscar']
        #Busco dentro del model Team:
        team= Team.objects.filter(escuderia=search)
        #Busco dentro del model empleado
        empleado = Empleado.objects.filter(nombre = search)
        #Busco dentro del model ingeniero
        ingeniero = Ingeniero.objects.filter(nombre = search)
        #Busco dentro del model piloto
        piloto = Piloto.objects.filter(nombre = search)
        #Busco dentro del model fans
        fan = Fan.objects.filter(nombre = search)
        #Busco dentro del model periodista
        periodista = Periodista.objects.filter(nombre = search)

        return render(request,'Resultados.html/', {"teams":team, 
                                                    "empleados": empleado,
                                                    "ingenieros":ingeniero,
                                                    "pilotos":piloto,
                                                    "Fans":fan,
                                                    "periodistas":periodista} )
    else:
        return render(request, 'Busqueda.html/', {"error": 'No hay datos'})
        