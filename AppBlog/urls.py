from django.urls import path
from AppBlog.views import *


urlpatterns = [
    path('home', home, name="Home"),
    path('posts', posts, name="Posts"),
    path('post/<int:post_id>', post, name="Posteo"),
    path('borrarpost/<int:post_id>', borrar_post, name="BorrarPost")
]