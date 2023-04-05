from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, "AppBlog/home.html", {"logeado":request.user.is_authenticated, "es_admin":request.user.is_staff})


def posts(request):
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, "AppBlog/posts.html")
    else:
        return redirect(reverse('Home'))