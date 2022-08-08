from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Creador(models.Model):

    nombre = models.CharField(max_length=50, default='')
    apellido=models.CharField(max_length=50, default='')
    descripcion = models.CharField(max_length=500, default='')

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
    
    def __str__(self):
        return (f'Nombre: {self.escuderia}.\nNacionalidad: {self.nacionalidad}.')

class Empleado(models.Model):
#La hago abstracta para que no genere una tabla innecesaria 
    
    nombre=  models.CharField(max_length=15, default='')
    apellido= models.CharField(max_length=15, default='')
    nacionalidad= models.CharField(max_length=25, default = '')
    experiencia= models.IntegerField(default=0)
    edad= models.IntegerField(default=0)  
    escuderia= models.CharField(max_length=25, default='')
    puesto= models.CharField(max_length=15, default='')
    email = models.EmailField()


    def __str__(self):
        return (f'Nombre: {self.nombre}.\nApellido: {self.apellido}.\nEscuderia: {self.escuderia}.\nPuesto: {self.puesto}.')

class Piloto(Empleado):
#Aqui agrego datos especificos de pilotos
    
    campeonatos_disputados= models.IntegerField(default=0)
    campeonatos_ganados= models.IntegerField(default=0)
    circuito_favorito = models.CharField(max_length=15)
    poles = models.IntegerField(default=0)
    carreras_disputadas= models.IntegerField(default=0)
    carreras_ganadas= models.IntegerField(default = 0)
    
class Ingeniero(Empleado):
#Agrego datos especificos de Ingenieros
    
    universidad= models.CharField(max_length=20, default='')
    titulo= models.CharField(max_length=20, default='')
    especialidad=  models.CharField(max_length=15, default='')
    ocupacion = models.CharField(max_length = 25, default='')

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

class Avatar(models.Model):
    
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    imagen=models.ImageField(upload_to='avatar/', null=True, blank=True)

class Publicaciones(models.Model):

    titulo = models.CharField(max_length= 50, default='')
    autor = models.CharField(max_length=25, default='')
    cuerpo = models.CharField(max_length=500, default='')
    fecha = models.DateField()

    def __str__(self):
        return (f'Titulo: {self.titulo}.\nAutor: {self.autor}.\nFecha: {self.fecha}')
    


