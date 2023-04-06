from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
    
class Usuario(AbstractUser):
    imagen = models.FileField(upload_to='imgs/usuarios')
    descripcion = models.CharField(max_length=256)
    link = models.CharField(max_length=256)

    def __str__(self) -> str:
        return "nombre: %s - email: %s - descripcion: %s - link: %s" % (self.username, self.email, self.descripcion, self.link)
