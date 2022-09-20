from django.shortcuts import redirect, render
from ProyectoFinalApp.forms import FormVehiculo, UserRegisterForm, MensajeForm, UpdateProfileForm, UpdateUserForm
from ProyectoFinalApp.models import Mensaje, Vehiculo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.defaults import page_not_found

def inicio(request):

    return render(request, 'ProyectoFinalApp/index.html')


def nosotros(request):
    
        return render(request, 'ProyectoFinalApp/about.html')


def modelos(request):
    
    vehiculos = Vehiculo.objects.all()
    if len(vehiculos) > 0:
        vehiculos = Vehiculo.objects.all()
        return render(request, 'ProyectoFinalApp/modelos.html', {'vehiculos': vehiculos})
    else:
        prueba = "No hay vehiculos"
        return render(request, 'ProyectoFinalApp/modelos.html', {'prueba': prueba})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
               return redirect("login")
        else:
            return redirect("login")

    form = AuthenticationForm()

    return render(request, 'ProyectoFinalApp/login.html', {'form': form})


def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        return render(request, "ProyectoFinalApp/register.html", {"form":form})

    form = UserRegisterForm()

    return render(request, 'ProyectoFinalApp/register.html', {'form': form})


def logout_request(request):
    logout(request)
    return redirect("inicio")


@staff_member_required
def panel(request):

    vehiculos = Vehiculo.objects.all()
    if len(vehiculos) > 0:
      vehiculos = Vehiculo.objects.all()
      return render(request, 'ProyectoFinalApp/panel.html', {'vehiculos': vehiculos})
    else:
        prueba = "No hay vehiculos"
        return render(request, 'ProyectoFinalApp/panel.html', {'prueba': prueba})


def detalle_vehiculo(request,vehiculoID):
    
    vehiculos = Vehiculo.objects.get(id=vehiculoID)
    return render(request, 'ProyectoFinalApp/detalle_vehiculo.html', {'vehiculos': vehiculos})


@staff_member_required
def eliminar_vehiculo(request, vehiculo_id):

    vehiculos = Vehiculo.objects.get(id=vehiculo_id)
    vehiculos.delete()

    return redirect("panel")
     

@staff_member_required
def crear_vehiculo(request):

    if request.method == "POST":

        formulario = FormVehiculo(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'El vehículo ha sido agregado correctamente')
            return redirect('panel')
    

    else:

        formularioVacio = FormVehiculo()

        return render(request,"ProyectoFinalApp/formulario_vehiculo.html",{"form":formularioVacio,"accion":"Crear Vehiculo"})


@staff_member_required
def editar_vehiculo(request, vehiculo_id):
    
    vehiculos = Vehiculo.objects.get(id=vehiculo_id)

    if request.method == "POST":

        formulario = FormVehiculo(request.POST, request.FILES, instance = vehiculos)
        if formulario.is_valid():
            
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'El vehículo ha sido editado correctamente')
            return redirect('panel')
        else:
            messages.add_message(request, messages.ERROR, 'El vehículo no ha sido editado')
    else:       
     formulario = FormVehiculo(instance=vehiculos)

    return render(request,"ProyectoFinalApp/formulario_vehiculo.html",{"form":formulario,"accion":"Editar Vehiculo"})


@login_required
def nuevo_mensaje(request):
    
   
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            nuevo_mensaje = form.save(commit = False)
            nuevo_mensaje.autor = request.user
            nuevo_mensaje.save()
            return redirect('mensajes_enviados')
    else:
        form = MensajeForm()
    ctx = {"form": form}
    return render(request, "ProyectoFinalApp/mensajes.html", ctx)


@login_required
def mensajes_recibidos(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    if len(mensajes_recibidos) > 0:
        mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
        return render(request, 'ProyectoFinalApp/mensajes_recibidos.html', {'mensajes_recibidos': mensajes_recibidos})
    else:
        prueba = "No hay mensajes recibidos"
        return render(request, 'ProyectoFinalApp/mensajes_recibidos.html', {'prueba': prueba})


@login_required
def mensajes_enviados(request):
    
    mensajes_enviados = Mensaje.objects.filter(autor=request.user)
    
    if len(mensajes_enviados) > 0:
        mensajes_enviados = Mensaje.objects.filter(autor=request.user)
        return render(request, 'ProyectoFinalApp/mensajes_enviados.html', {'mensajes_enviados': mensajes_enviados})
    else:
        prueba = "No hay mensajes enviados"
        return render(request, 'ProyectoFinalApp/mensajes_enviados.html', {'prueba': prueba})


@login_required
def profile(request):
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado con éxito')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'ProyectoFinalApp/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class CambiarContraseña(SuccessMessageMixin, PasswordChangeView):
    template_name = 'ProyectoFinalApp/cambiar_contraseña.html'
    success_message = 'Cambiaste tu contraseña con éxito'
    success_url = reverse_lazy('profile')
 

def error_404_view(request, exception):
   
    return render(request, '404.html')
