from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from AppLogin.views import *


urlpatterns = [
    path('accounts/login', login_request, name="Login"),
    path('accounts/signup', registro, name="Registro"),
    path('logout', logout_request, name="Logout"),
]