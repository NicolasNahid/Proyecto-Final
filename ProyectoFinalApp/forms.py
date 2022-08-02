from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ProyectoFinalApp.models import Mensaje, Profile, Vehiculo

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FormVehiculo(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ['modelo', 'resumen', 'descripcion', 'categoria', 'foto']       

      
class MensajeForm(forms.ModelForm):
    
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido']

      
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']