from django.urls import path
from AppBlog.views import *


urlpatterns = [
    path('home', home, name="Home"),
    path('posts', posts, name="Posts"),
]