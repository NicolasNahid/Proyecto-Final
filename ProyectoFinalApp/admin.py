from django.contrib import admin

from.models import *
# Register your models here.


class VehiculoAdmin(admin.ModelAdmin):

    list_display = ('modelo', 'resumen', 'fecha_creacion','descripcion', 'categoria', 'foto')
    search_fields = ('modelo', 'resumen')


admin.site.register(Vehiculo, VehiculoAdmin)
