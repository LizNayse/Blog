from django.db import models
import datetime

# Create your models here.

class Posteo(models.Model):
 
    titulo=models.CharField(max_length=256)
    #imagen=models.ImageField()
    contenido=models.CharField(max_length=5000)
    fecha=models.DateTimeField(default=datetime.datetime.now)
    autor=models.CharField(max_length=256)

    def __str__(self) -> str:
        return "%s-%s-%s" %(self.titulo, self.contenido, str(self.fecha))

class Comentario(models.Model):

    post=models.ForeignKey(
        Posteo,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    contenido=models.CharField(max_length=5000)
    fecha=models.DateTimeField(default=datetime.datetime.now)
    autor=models.CharField(max_length=256)

class RespuestaComentario(models.Model):
        
    comentario=models.OneToOneField(
        Comentario,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    contenido=models.CharField(max_length=5000)
    fecha=models.DateTimeField(default=datetime.datetime.now)
    autor=models.CharField(max_length=256)
