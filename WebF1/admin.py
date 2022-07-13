from django.contrib import admin
from WebF1.views import Escuderias
from .models import *
# Register your models here.

admin.site.register(Team)
admin.site.register(Empleado)
admin.site.register(Ingeniero)
admin.site.register(Piloto)
admin.site.register(Periodista)
admin.site.register(Fan)