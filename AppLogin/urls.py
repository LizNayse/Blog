from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from AppLogin.views import *


urlpatterns = [
    path('login', login_request, name="Login"),
    path('registro', registro, name="Registro"),
    path('logout', logout_request, name="Logout"),
]