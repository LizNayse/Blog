from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from .forms import CrearPostForm, EditarDatosForm, CambiarContraseniaForm
from .models import Posteo, Comentario, RespuestaComentario
from django.contrib.auth.decorators import login_required, permission_required


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
        return render(request, "AppBlog/crear_post.html", {"logeado":request.user.is_authenticated, "es_admin":request.user.is_staff, "form": form})
    else:
        return redirect(reverse('Home'))


def puede_comentar_post(request):
    return request.user.is_authenticated and not request.user.is_staff


def post(request, post_id):
    posteo = Posteo.objects.get(id=post_id)
    return render(request, "AppBlog/post.html", { "logeado":request.user.is_authenticated, "es_admin": request.user.is_staff, "post":posteo , "puede_comentar": puede_comentar_post(request) })


@login_required(login_url="Login")
@permission_required("is_staff", raise_exception=True)
def borrar_post(request, post_id):
    posteo = Posteo.objects.get(id=post_id)
    posteo.delete()
    return redirect(reverse('Home'))


@login_required(login_url="Login")
def comentar_post(request, post_id):
    posteo = Posteo.objects.get(id=post_id)
    contenido = request.POST['contenido']
    comentario = Comentario (post = posteo, contenido = contenido, autor = request.user.username)
    comentario.save()
    return redirect(reverse('Posteo', kwargs={ "post_id": post_id }))


@login_required(login_url="Login")
@permission_required("is_staff", raise_exception=True)
def borrar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    posteo = comentario.post
    comentario.delete()
    return redirect(reverse('Posteo', kwargs={ "post_id": posteo.id }))


@login_required(login_url="Login")
@permission_required("is_staff", raise_exception=True)
def responder_comentario(request, comentario_id):
    contenido = request.POST['contenido']
    comentario = Comentario.objects.get(id=comentario_id)
    posteo = comentario.post
    respuesta = RespuestaComentario (comentario = comentario, contenido = contenido, autor = request.user.username)
    respuesta.save()
    return redirect(reverse('Posteo', kwargs={ "post_id": posteo.id }))


@login_required(login_url="Login")
@permission_required("is_staff", raise_exception=True)
def borrar_respuesta(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    posteo = comentario.post
    comentario.respuestacomentario.delete()
    return redirect(reverse('Posteo', kwargs={ "post_id": posteo.id }))


@login_required(login_url="Login")
def perfil(request):
    return render(request, "AppBlog/perfil.html", { "logeado":request.user.is_authenticated, "es_admin": request.user.is_staff, "perfil": request.user })


@login_required(login_url="Login")
def editar_datos(request):
    usuario = request.user
    datos_usuario = {
            'email': usuario.email,
            'imagen': usuario.imagen,
            'descripcion': usuario.descripcion,
            'link': usuario.link
    }
    if request.method == "POST":
        form = EditarDatosForm(request.POST, request.FILES, initial=datos_usuario)
        if form.is_valid():
            nuevo_email = form.cleaned_data.get('email')
            nueva_descripcion = form.cleaned_data.get('descripcion')
            nuevo_link = form.cleaned_data.get('link')
            nueva_imagen = form.cleaned_data.get('imagen')
            usuario.email = nuevo_email
            usuario.descripcion = nueva_descripcion
            usuario.link = nuevo_link
            usuario.imagen = nueva_imagen
            usuario.save()
            return redirect(reverse('VerPerfil'))
    else:
        form = EditarDatosForm(initial=datos_usuario)
    return render(request, "AppBlog/perfil.html", { "logeado":request.user.is_authenticated, "es_admin": request.user.is_staff, "perfil": usuario, "form": form })


@login_required(login_url="Login")
def cambiar_contrasenia(request):
    usuario = request.user
    if request.method == "POST":
        form = CambiarContraseniaForm(usuario, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, usuario)
            return redirect(reverse('VerPerfil'))
    else:
        form = CambiarContraseniaForm(usuario)
    return render(request, "AppBlog/cambiar_contrasenia.html", { "logeado":request.user.is_authenticated, "es_admin": request.user.is_staff, "form": form })


def acerca_de(request):
    return render(request, "AppBlog/about_us.html", { "logeado":request.user.is_authenticated, "es_admin": request.user.is_staff, "perfil": request.user })