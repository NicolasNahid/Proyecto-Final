from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ProyectoFinalApp.models import vehiculo

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class FormVehiculo(forms.Form):
    modelo = forms.CharField(max_length=50)
    resumen = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=500,widget=forms.Textarea)
    fecha_creacion =  forms.DateTimeField(initial="")
    categoria = forms.CharField(max_length=20)
    foto = forms.ImageField()

    class Meta:
        model = vehiculo
        fields = ['modelo', 'resumen', 'descripcion', 'fecha_creacion', 'categoria', 'foto']