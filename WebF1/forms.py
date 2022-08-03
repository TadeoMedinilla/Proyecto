from django import forms

from WebF1.models import Ingeniero, Piloto

# Create your models here.
class TeamForm(forms.Form):
   
    escuderia = forms.CharField(max_length=15)
    nacionalidad = forms.CharField(max_length=20 )
    patrocinador = forms.CharField(max_length=20)
    proovedor_motor = forms.CharField(max_length=20)
    modelo_del_motor= forms.CharField(max_length=20)
    proovedor_chasis =  forms.CharField(max_length=20)
    modelo_chasis= forms.CharField(max_length=20)
    gp_anfitrion= forms.CharField(max_length=20)
    piloto_principal= forms.CharField(max_length=20)
    piloto_secundario= forms.CharField(max_length=20)
    cantidad_de_empleados= forms.IntegerField()
'''
class EmpleadoForm():

    nombre=  forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    edad= forms.IntegerField()
    puesto= forms.CharField(max_length=20)

class PilotoForm(EmpleadoForm):

    experiencia= forms.IntegerField()
    campeonatos_disputados= forms.IntegerField()
    campeonatos_ganados= forms.IntegerField()
    circuito_favorito= forms.CharField(max_length=15)
    
class IngenieroForm(EmpleadoForm):

    universidad= forms.CharField(max_length=20)
    titulo= forms.CharField(max_length=20)
    especialidad=  forms.CharField(max_length=15)
    experiencia= forms.IntegerField()
    email= forms.EmailField()

'''

class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields= ['nombre', 'apellido', 'nacionalidad',
                    'experiencia', 'edad', 'escuderia',
                    'puesto', 'campeonatos_disputados',
                    'campeonatos_ganados',
                     'carreras_disputadas', 'carreras_ganadas',
                     'poles', 'circuito_favorito','email']

class IngenieroForm(forms.ModelForm):
    class Meta:
        model = Ingeniero
        fields= ['nombre', 'apellido', 'nacionalidad',
                    'experiencia', 'edad', 'escuderia',
                    'puesto', 'universidad','titulo',
                     'especialidad', 'ocupacion','email']

class PeriodistaForm(forms.Form):

    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    medio= forms.CharField(max_length=20)
    matricula= forms.IntegerField()
    email= forms.EmailField()

class FanForm(forms.Form):

    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    email= forms.EmailField()
    edad= forms.IntegerField() 