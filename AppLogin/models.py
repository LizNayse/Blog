from django.db import models

# Create your models here.

class Usuario(models.Model):

    usuario=models.CharField(max_length=256)
    contrasenia=models.CharField(max_length=8)
    email=models.EmailField()

    def __str__(self) -> str:
        return self.usuario