from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from ProyectoFinalApp.models import Mensaje, Vehiculo

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