from ast import Name
import py_compile
from re import template
from django.urls import path
from WebF1 import views

from .views import AboutUs, AgregarAvatar, DetalleUsuario, Inicio, Busqueda, Buscar, Login, ModificarUsuario, MostrarPublicaciones, Publicacion, Register
from django.contrib.auth.views import LogoutView
#Importo CRUD Publicaciones 
from .views import Publicacion, MostrarPublicaciones, EliminarPublicacion, DetallePublicacion
#Importo CRUD Escuderias
from .views import Escuderias, LeerEscuderias, ModificarEscuderia, EliminarEscuderia, DetalleEscuderia
#Importo CRUD Pilotos
from .views import Pilotos, LeerPilotos, ModificarPiloto, EliminarPiloto, DetallePiloto
#Importo CRUD Ingenieros
from .views import Ingenieros, LeerIngenieros, ModificarIngeniero, EliminarIngeniero, DetalleIngeniero
#Importo CRUD Fans
from .views import Fans, MostrarFans, ModificarFan, EliminarFan, DetalleFan
#Importo CRUD Periodistas
from .views import Periodistas, MostrarPeriodistas, ModificarPeriodista, EliminarPeriodista, DetallePeriodista


urlpatterns = [

    path('', Inicio, name= 'Inicio'),
    path('AboutUs/', AboutUs, name= 'AboutUs'),

    path("Busqueda/", Busqueda, name= 'Busqueda'),
    path('Buscar/', Buscar, name= 'Buscar'),
    
    #Urls CRUD Publicaciones:
    path('Publicaciones/', Publicacion, name= 'Publicaciones'),
    path('MostrarPublicaciones/', MostrarPublicaciones, name='MostrarPublicaciones'),
    path('EliminarPublicacion/<pk>', EliminarPublicacion.as_view(), name='EliminarPublicacion'),
    path('DetallePublicacion/<pk>', DetallePublicacion.as_view(), name='DetallePublicacion'),

    #Urls CRUD Login:
    path('Login/', Login, name= 'Login'),
    path('Register/', Register, name= 'Register'),
    path('Logout/', LogoutView.as_view(template_name = 'Logout.html'), name='Logout'),
    path('ModificarUsuario/<pk>', ModificarUsuario, name= 'ModificarUsuario'),
    path('DetalleUsuario/<pk>', DetalleUsuario.as_view() , name= 'DetalleUsuario'),
    path('AgregarAvatar/', AgregarAvatar, name= 'AgregarAvatar'),

    #Urls CRUD Escuderias:
    path('Escuderias/', Escuderias, name= 'Escuderias'),
    path('MostrarEscuderias/', LeerEscuderias, name= 'MostrarEscuderias'),
    path('EliminarEscuderia/<pk>', EliminarEscuderia, name= 'EliminarEscuderia'),
    path('ModificarEscuderia/<pk>', ModificarEscuderia, name= 'ModificarEscuderia'),
    path('DetalleEscuderia/<pk>', DetalleEscuderia.as_view(), name= 'DetalleEscuderia'),
    
    #Urls CRUD Pilotos:
    path('Pilotos/', Pilotos, name= 'Pilotos'),
    path('MostrarPilotos/', LeerPilotos, name= 'MostrarPilotos'),
    path('EliminarPiloto/<pk>/', EliminarPiloto, name= 'EliminarPiloto'),
    path('ModificarPiloto/<pk>/', ModificarPiloto, name= 'ModificarPiloto'),
    path('DetallePiloto/<pk>', DetallePiloto.as_view(), name= 'DetallePiloto'),
    
    #Urls CRUD Ingenieros:
    path('Ingenieros/', Ingenieros, name= 'Ingenieros'),
    path('MostrarIngenieros/', LeerIngenieros, name= 'MostrarIngenieros'),
    path('ModificarIngeniero/<pk>/', ModificarIngeniero, name= 'ModificarIngeniero'),
    path('EliminarIngeniero/<pk>/', EliminarIngeniero, name= 'EliminarIngeniero'),
    path('DetalleIngeniero/<pk>', DetalleIngeniero.as_view(), name= 'DetalleIngeniero'),
    
    #Urls CRUD fans:
    path('Fans/', Fans.as_view(), name= 'Fans'),
    path('MostrarFans/', MostrarFans.as_view(), name='MostrarFans'),
    path('ModificarFan/<pk>', ModificarFan.as_view(), name= 'ModificarFan'),
    path('EliminarFan/<pk>', EliminarFan.as_view(), name= 'EliminarFan'),
    path('DetalleFan/<pk>', DetalleFan.as_view(), name= 'DetalleFan'),

    #Urls CRUD periodistas:
    path('Periodistas/', Periodistas.as_view(), name= 'Periodistas'),
    path('MostrarPeriodistas/', MostrarPeriodistas.as_view(), name= 'MostrarPeriodistas'),
    path('ModificarPeriodista/<pk>', ModificarPeriodista.as_view(), name= 'ModificarPeriodista'),
    path('EliminarPeriosita/<pk>', EliminarPeriodista.as_view(), name= 'EliminarPeriodista'),
    path('DetallePeriodista/<pk>', DetallePeriodista.as_view(), name= 'DetallePeriodista'),
    ]