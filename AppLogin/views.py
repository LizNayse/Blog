from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from AppLogin.forms import UserRegisterForm
from django.urls import reverse

# Create your views here.
def login_request(request):

    form = AuthenticationForm(request, data = request.POST)

    if request.method == "POST":
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return redirect(reverse('Home'))
            else:
                return render(request, "AppLogin/login.html", {"mensaje":"Datos incorrectos", 'form':form})
        else:
            
            return render(request, "AppLogin/login.html", {"mensaje":"Formulario incorrectos", 'form':form})

    return render(request, "AppLogin/login.html", {'form':form})


def registro(request):

    form = UserRegisterForm(request.POST)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password1')
            user = authenticate(username=usuario, password=contrasenia)
            login(request, user)
            return redirect(reverse('Home'))
    
    return render(request, "AppLogin/registro.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect(reverse('Home'))