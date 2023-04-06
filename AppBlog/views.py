from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Posteo, Comentario, RespuestaComentario
from django.http import HttpResponse
from .forms import CrearPostForm

# Create your views here.
def home(request):
    posts = Posteo.objects.all
    return render(request, "AppBlog/home.html", {"logeado":request.user.is_authenticated, "es_admin":request.user.is_staff, "posts":posts})


def posts(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == "POST":
            form = CrearPostForm(request.POST, request.FILES)
            if form.is_valid():
                titulo = request.POST['titulo']
                contenido = request.POST['contenido']
                imagen = request.FILES['imagen']
                post = Posteo (titulo=titulo, contenido=contenido, autor=request.user.username, imagen = imagen)
                post.save()
                return redirect(reverse('Home'))
        else:
            form = CrearPostForm()
        return render(request, "AppBlog/crear_post.html", {'form': form})
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


def borrar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    posteo = comentario.post
    comentario.delete()
    return redirect(reverse('Posteo', kwargs={"post_id": posteo.id}))


def responder_comentario(request, comentario_id):
    contenido = request.POST['contenido']
    comentario = Comentario.objects.get(id=comentario_id)
    posteo = comentario.post
    respuesta = RespuestaComentario (comentario = comentario, contenido = contenido, autor = request.user.username)
    respuesta.save()
    return redirect(reverse('Posteo', kwargs={"post_id": posteo.id}))


def borrar_respuesta(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    posteo = comentario.post
    comentario.respuestacomentario.delete()
    return redirect(reverse('Posteo', kwargs={"post_id": posteo.id}))
