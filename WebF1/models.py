from django.db import models

# Create your models here.
class Team(models.Model):

    Categoria= 'Formula 1'
    Deporte = 'Automovilismo'
    Temporada = 2022 #Tuve problemas con la libreria datetime por eso no la use.
    
    escuderia = models.CharField(max_length=10, default='')
    nacionalidad = models.CharField(max_length=15, default='')
    patrocinador = models.CharField(max_length=15, default='')
    proov_motor = models.CharField(max_length=15, default='')
    mod_motor= models.CharField(max_length=15, default='')
    proov_chasis =  models.CharField(max_length=15, default='')
    mod_chasis= models.CharField(max_length=15, default='')
    gp_anfitrion= models.CharField(max_length=15, default='')
    pil_ppal= models.CharField(max_length=15, default='')
    pil_sec= models.CharField(max_length=15, default='')
    cant_emp= models.IntegerField(default=0)

class Empleado(Team):
#Me interesa heredar de Team: escuderia, categoria, deporte y temporada
    nombre=  models.CharField(max_length=15, default='')
    apellido= models.CharField(max_length=15, default='')
    edad= models.IntegerField(default=0)  
    puesto= models.CharField(max_length=15, default='')

class Piloto(Empleado):
#Me interesa heredar: datos personales y escuderia
    exp= models.IntegerField(default=0)
    camp_disp= models.IntegerField(default=0)
    camp_gan= models.IntegerField(default=0)
    circuito = models.CharField(max_length=15)
    
class Ingeniero(Empleado):
#Me interesa heredar: datos personales y escuderia
    universidad= models.CharField(max_length=20)
    titulo= models.CharField(max_length=20)
    especialidad=  models.CharField(max_length=15)
    exp= models.IntegerField(default=0)
    email= models.EmailField()

class Periodista(models.Model):

    nombre= models.CharField(max_length=20, default='')
    apellido=models.CharField(max_length=20, default='')
    medio=models.CharField(max_length=20, default='')
    matricula=models.IntegerField(default=0)
    email= models.EmailField()

class Fan(models.Model):

    nombre= models.CharField(max_length=20, default='')
    apellido=models.CharField(max_length=20, default='')
    email= models.EmailField(default=None)
    edad= models.IntegerField(default=0)