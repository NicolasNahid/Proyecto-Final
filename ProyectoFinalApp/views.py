from email.mime import image
from django.forms import ImageField
from django.shortcuts import redirect, render

from ProyectoFinalApp.forms import FormVehiculo, UserRegisterForm

from ProyectoFinalApp.models import vehiculo

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def inicio(request):

    return render(request, 'ProyectoFinalApp/index.html')


def nosotros(request):
    
        return render(request, 'ProyectoFinalApp/about.html')


def modelos(request):
    
    vehiculos = vehiculo.objects.all()
    if len(vehiculos) > 0:
        vehiculos = vehiculo.objects.all()
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

    vehiculos = vehiculo.objects.all()
    if len(vehiculos) > 0:
      vehiculos = vehiculo.objects.all()
      return render(request, 'ProyectoFinalApp/panel.html', {'vehiculos': vehiculos})
    else:
        prueba = "No hay vehiculos"
        return render(request, 'ProyectoFinalApp/panel.html', {'prueba': prueba})
    
@login_required
def profile(request):

    return render(request, 'ProyectoFinalApp/profile.html')


def detalle_vehiculo(request,vehiculoID):
    
    vehiculos = vehiculo.objects.get(id=vehiculoID)
    return render(request, 'ProyectoFinalApp/detalle_vehiculo.html', {'vehiculos': vehiculos})


@staff_member_required
def eliminar_vehiculo(request, vehiculo_id):

    vehiculos = vehiculo.objects.get(id=vehiculo_id)
    vehiculos.delete()

    return redirect("panel")
     

@staff_member_required
def crear_vehiculo(request):

    if request.method == "POST":

        formulario = FormVehiculo(request.POST)

        if formulario.is_valid():

            info_art = formulario.cleaned_data
        
            nuevo = vehiculo(modelo=info_art["modelo"], resumen=info_art["resumen"], descripcion=info_art["descripcion"],
            categoria=info_art["categoria"], foto=formulario.cleaned_data["foto"])

            nuevo.save() 
            messages.add_message(request, messages.SUCCESS, 'El vehículo ha sido agregado correctamente')
            return redirect('panel')

        else:
            messages.add_message(request, messages.ERROR, 'El vehículo no ha sido agregado')
            return render(request,"ProyectoFinalApp/formulario_vehiculo.html",{"form":formulario,"accion":"Crear Vehiculo"})
    

    else:

        formularioVacio = FormVehiculo()

        return render(request,"ProyectoFinalApp/formulario_vehiculo.html",{"form":formularioVacio,"accion":"Crear Vehiculo"})

@staff_member_required
def editar_vehiculo(request, vehiculo_id):
    
    vehiculos = vehiculo.objects.get(id=vehiculo_id)

    if request.method == "POST":

        formulario = FormVehiculo(request.POST)

        if formulario.is_valid():

            info_art = formulario.cleaned_data
        
            vehiculos.modelo = info_art["modelo"]
            vehiculos.resumen = info_art["resumen"]
            vehiculos.descripcion = info_art["descripcion"]
            vehiculos.fecha_creacion = info_art["fecha_creacion"]
            vehiculos.categoria = info_art["categoria"]
            vehiculos.foto = ImageField()["foto"]
            vehiculos.save()
            messages.add_message(request, messages.SUCCESS, 'El vehículo ha sido editado correctamente')
            return redirect('panel')
        else:
            messages.add_message(request, messages.ERROR, 'El vehículo no ha sido editado')
    else:       
     formulario = FormVehiculo(initial={"modelo":vehiculos.modelo,"resumen":vehiculos.resumen,"descripcion":vehiculos.descripcion,
     "fecha_creacion":vehiculos.fecha_creacion, "categoria":vehiculos.categoria, "foto":vehiculos.foto})

    return render(request,"ProyectoFinalApp/formulario_vehiculo.html",{"form":formulario,"accion":"Editar Vehiculo"})
    