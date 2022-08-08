from django.shortcuts import render
from .formsMensajeria import *
from datetime import date, datetime
from django.contrib.auth.models import User


#Enviar el mensaje:
def Mensaje(request):
    if request.method == 'POST':

        MiForm = MensajeForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:

            info = MiForm.cleaned_data
            mensaje = Mensajes( autor = info['autor'], 
                                destinatario = info['destinatario'],
                                cuerpo = info['cuerpo'],
                                leido = False,
                                fecha = date.today() )
            
            mensaje.save()
            usuarios = User.objects.all()
            notificacion = 'Mensaje enviado.'
            lista = {'users': usuarios, 'notificacion':notificacion}
 
            return render(request, 'Inicio.html', lista)
    else:
        usuarios = User.objects.all()
        
        MiForm = MensajeForm()
    
    return render(request, 'MensajeNuevo.html', {'MiForm': MiForm, 'users': usuarios}) 

# Read:
def MostrarMensajes(request, username):

    mensajes = Mensajes.objects.filter(destinatario = username)
    modelo = {'mensajes':mensajes}

    return render(request, 'MostrarMensajes.html', modelo)

def ResponderMensajes(request,pk):

    mensaje=Mensajes.objects.get(pk=pk)
    
    if mensaje.leido==False:
        mensaje.leido=True
        mensaje.save()
    

    if request.method == 'POST':
        MiForm = MensajeForm(request.POST)
        print(MiForm)

        if MiForm.is_valid:
            info = MiForm.cleaned_data
            m = Mensajes(autor=info['destinatario'],
                        destinatario= info['autor'],
                        cuerpo=info['cuerpo'],
                        fecha=datetime.now(),
                        leido=False)
            
            m.save()

            mensajes = Mensajes.objects.filter(destinatario = m.autor)
            notificacion = 'Mensaje enviado.'
            
            modelo={'mensajes':mensajes, 'notificacion':notificacion}

            return render(request, 'MostrarMensajes.html', modelo)

    else:
        MiForm= MensajeForm(initial={'autor':mensaje.destinatario, 
                                        'destinatario': mensaje.autor})
            
    return render(request, 'ResponderMensaje.html', {'MiForm':MiForm,'mensaje':mensaje})

def EliminarMensaje(request,pk):

    mensaje = Mensajes.objects.get(pk = pk)
    mensaje.delete()

    mensajes = Mensajes.objects.filter(destinatario = mensaje.destinatario)
    notificacion='Mensaje eliminado.'
    modelo = {'mensajes':mensajes, 'notificacion':notificacion}

    return render(request, 'MostrarMensajes.html', modelo)