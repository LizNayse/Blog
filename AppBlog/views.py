from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Posteo, Comentario
from django.http import HttpResponse

# Create your views here.
def home(request):
    posts = Posteo.objects.all
    return render(request, "AppBlog/home.html", {"logeado":request.user.is_authenticated, "es_admin":request.user.is_staff, "posts":posts})


def posts(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            titulo = request.POST['titulo']
            contenido = request.POST['contenido']
            post = Posteo (titulo=titulo, contenido=contenido, autor=request.user.username)
            post.save()
            return redirect(reverse('Home'))
        return render(request, "AppBlog/crear_post.html")
    else:
        return redirect(reverse('Home'))


def puede_comentar_post(request):
    return request.user.is_authenticated and not request.user.is_staff


def post(request, post_id):
    posteo = Posteo.objects.get(id=post_id)
    return render(request, "AppBlog/post.html", { "es_admin": request.user.is_staff, "post":posteo , "puede_comentar": puede_comentar_post(request) })


def borrar_post(request, post_id):
    posteo = Posteo.objects.get(id=post_id)
    posteo.delete()
    return redirect(reverse('Home'))


def comentar_post(request, post_id):
    posteo = Posteo.objects.get(id=post_id)
    contenido = request.POST['contenido']
    comentario = Comentario (post = posteo, contenido = contenido, autor = request.user.username)
    comentario.save()
    return redirect(reverse('Posteo', kwargs={"post_id": post_id}))
