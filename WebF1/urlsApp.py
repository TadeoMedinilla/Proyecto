from ast import Name
import py_compile
from django.urls import path
from WebF1 import views
from .views import Inicio, Escuderias, Ingenieros, Pilotos, Fans, Periodistas
from .views import Busqueda, Buscar

urlpatterns = [
    path('', Inicio, name= 'Inicio'),
    path('Escuderias/', Escuderias, name= 'Escuderias'),
    path('Ingenieros/', Ingenieros, name= 'Ingenieros'),
    path('Pilotos/', Pilotos, name= 'Pilotos'),
    path('Fans/', Fans, name= 'Fans'),
    path('Periodistas/', Periodistas, name= 'Periodistas'),
    path("Busqueda", Busqueda, name= 'Busqueda'),
    path('Buscar/', Buscar),
    
    ]