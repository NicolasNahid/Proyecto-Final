from django.contrib import admin
from .models import *


class VehiculoAdmin(admin.ModelAdmin):

    list_display = ('modelo', 'resumen', 'fecha_creacion','descripcion', 'categoria', 'foto')
    search_fields = ('modelo', 'resumen')


admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Profile)
