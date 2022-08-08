from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Mensajes(models.Model):

    leido = models.BooleanField()
    autor = models.CharField(max_length=25, default='')
    destinatario = models.CharField(max_length= 25, default='')
    cuerpo = RichTextField(blank = True , null =True)
    # cuerpo = models.CharField(max_length=500, default='')
    fecha = models.DateField()

    def __str__(self):
        return (f'Mensaje de: {self.autor}.||\nPara: {self.destinatario}  || \nCuerpo: {self.cuerpo}.')