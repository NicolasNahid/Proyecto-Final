from django.db import models


# Create your models here.


class vehiculo(models.Model):
    modelo = models.CharField(max_length=50)
    resumen = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=20)
    foto = models.ImageField()
    
   

    def __str__(self):
        return self.modelo

    class Meta:
        verbose_name = 'vehiculo'
        verbose_name_plural = 'vehiculos'
