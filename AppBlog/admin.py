from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Posteo)
admin.site.register(Comentario)
admin.site.register(RespuestaComentario)