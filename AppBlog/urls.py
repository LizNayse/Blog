from django.urls import path
from AppBlog.views import *


urlpatterns = [
    path('home', home, name="Home"),
    path('posts', posts, name="Posts"),
    path('post/<int:post_id>', post, name="Posteo"),
    path('borrarpost/<int:post_id>', borrar_post, name="BorrarPost"),
    path('comentarpost/<int:post_id>', comentar_post, name="ComentarPost"),
    path('borrarcomentario/<int:comentario_id>', borrar_comentario, name="BorrarComentario")
]