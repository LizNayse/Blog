from django.urls import path
from AppBlog.views import *


urlpatterns = [
    path('pages', home, name="Home"),
    path('posts', posts, name="Posts"),
    path('pages/<int:post_id>', post, name="Posteo"),
    path('borrarpost/<int:post_id>', borrar_post, name="BorrarPost"),
    path('comentarpost/<int:post_id>', comentar_post, name="ComentarPost"),
    path('borrarcomentario/<int:comentario_id>', borrar_comentario, name="BorrarComentario"),
    path('respondercomentario/<int:comentario_id>', responder_comentario, name="ResponderComentario"),
    path('borrarrespuesta/<int:comentario_id>', borrar_respuesta, name="BorrarRespuesta"),
    path('perfil', perfil, name="VerPerfil"),
    path('editardatos', editar_datos, name="EditarDatos"),
    path('cambiarcontrasenia', cambiar_contrasenia, name="CambiarContrasenia"),
    path('about', acerca_de, name="AcercaDe")
]