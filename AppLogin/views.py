from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from AppLogin.forms import UserRegisterForm

# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render (request, "AppLogin/login.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppLogin/login.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AppLogin/login.html", {"mensaje":"Formulario incorrectos"})
    
    form = AuthenticationForm()

    return render(request, "AppLogin/login.html", {'form':form})

def registro(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppLogin/registro.html", {"mensaje": "Usuario creado :D"})
    
    else:
        form = UserRegisterForm()
    
    return render(request, "AppLogin/registro.html", {"form":form})