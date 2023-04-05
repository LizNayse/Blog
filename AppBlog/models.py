from django.db import models

# Create your models here.

class Post(models.Model):
 
    titulo=models.CharField(max_length=256)
    #imagen=models.ImageField()
    contenido=models.CharField(max_length=5000)
    fecha=models.DateTimeField()
    autor=models.CharField(max_length=256)

class Comentario(models.Model):

    post=models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    contenido=models.CharField(max_length=5000)
    fecha=models.DateTimeField()
    autor=models.CharField(max_length=256)

class RespuestaComentario(models.Model):
        
    comentario=models.OneToOneField(
        Comentario,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    contenido=models.CharField(max_length=5000)
    fecha=models.DateTimeField()
    autor=models.CharField(max_length=256)
