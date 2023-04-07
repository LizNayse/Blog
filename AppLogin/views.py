from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from AppLogin.forms import UserRegisterForm
from django.urls import reverse

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
                return redirect(reverse('Home'))
            else:
                return render(request, "AppLogin/login.html", {'form':form})
        else:
            
            return render(request, "AppLogin/login.html", {'form':form})
    else:
        form = AuthenticationForm(request)
    return render(request, "AppLogin/login.html", {'form':form})


def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password1')
            user = authenticate(username=usuario, password=contrasenia)
            login(request, user)
            return redirect(reverse('Home'))
    else:
        form = UserRegisterForm()
    return render(request, "AppLogin/registro.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect(reverse('Home'))