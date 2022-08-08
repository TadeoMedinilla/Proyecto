from dataclasses import fields
from tkinter.ttk import Style
from django import forms

from .modelsMensajeria import *

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensajes
        fields = ['autor', 'destinatario' , 'leido', 'cuerpo','fecha']
        