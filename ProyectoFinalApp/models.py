from django.db import models
from django.contrib.auth.models import User


class Vehiculo(models.Model):
    modelo = models.CharField(max_length=50) # test +50ch
    resumen = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True) # test numero random
    categoria = models.CharField(max_length=20) # test +20ch
    foto = models.ImageField(upload_to="modelos", null=True, blank=True)
    

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'


class Mensaje(models.Model):
    autor = models.ForeignKey(User, related_name = "autor", on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name = "destinatario", on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    asunto = models.CharField(max_length=200)
    
    
    def __str__(self):
        return f"{self.fecha_hora} de: {self.autor}, asunto: {self.asunto}"
    
    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

