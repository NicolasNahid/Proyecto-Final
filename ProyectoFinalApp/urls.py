from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"),
    path('nosotros/', nosotros, name="nosotros"),
    path('modelos/', modelos, name="modelos"),
    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    path('panel/', panel, name="panel"),
    path('profile/', profile, name="profile"),
    path('detalle_vehiculo/<vehiculoID>', detalle_vehiculo, name="detalle_vehiculo"),
    path('eliminar_vehiculo/<vehiculo_id>', eliminar_vehiculo, name="eliminar_vehiculo"),
    path('formulario_vehiculo/', crear_vehiculo, name="crear_vehiculo"),
    path('editar_vehiculo/<vehiculo_id>', editar_vehiculo, name="editar_vehiculo"),
    path('mensajes/', nuevo_mensaje, name="mensajes"),
    path('mensajes_recibidos/', mensajes_recibidos, name="mensajes_recibidos"),
    path('mensajes_enviados/', mensajes_enviados, name="mensajes_enviados"),
    
]