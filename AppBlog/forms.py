from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from AppLogin.models import Usuario

class CrearPostForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    contenido = forms.CharField(max_length=200)
    imagen = forms.FileField()


class EditarDatosForm(forms.Form):
    email = forms.EmailField(max_length=256, required=False)
    imagen = forms.FileField(required=False, widget=forms.FileInput)
    descripcion = forms.CharField(max_length=256, required=False)
    link = forms.CharField(max_length=256, required=False)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ("imagen", "descripcion", "link")


class CambiarContraseniaForm(PasswordChangeForm):
    class Meta:
        model = Usuario
