from django import forms

class CrearPostForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    contenido = forms.CharField(max_length=200)
    imagen = forms.FileField()