from django.shortcuts import redirect, render
from .models import Vehiculo,User
from .forms import USerForms, VehiculoForms

# Create your views here.

def mostrar(request):
    vehiculo = Vehiculo.objects.all() 
    user= User.objects.all() 
    return render(request,'core/mostar.html', context={'Datos':vehiculo, 'User':user})




def inicio(request):
    return render(request,'inicio.html')

def quienes_somos(request):
    return render(request,'quienes-somos.html')

def galeria_foto(request):
    return render(request,'galeria-fotografica.html')

def registro(request):
    return render(request,'core/registro.html')

def competencias(request):
    return render(request,'competencias.html')     


def form_vehiculo(request):
    if request.method == "POST":
        vehiculo_form = VehiculoForms(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return redirect('core/mostrar')
    else:
        vehiculo_form = VehiculoForms()        
    return render(request,'core/registro.html',{'vehiculo_form':vehiculo_form})

def form_user(request):
    if request.method == "POST":
        user_form = USerForms(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('core/mostrar')
    else:
        user_form = USerForms()        
    return render(request,'core/registro.html',{'user_form':user_form})

def form_modificar_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)

    datos = {
        'form': VehiculoForms(instance=vehiculo)
    }
    if request.method == 'POST':
        formulario = VehiculoForms(data=request.POST, instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    return render(request, 'core/form_mod_vehiculo.html', datos)   

def form_modificar_usuario(request,id):
    user = User.objects.get(idUser=id)

    datos = {
        'form': USerForms(instance=user)
    }
    if request.method == 'POST':
        formulario = VehiculoForms(data=request.POST, instance=user)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    return render(request, 'core/form_mod_usuario.html', datos)

def form_eliminar_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect('mostrar')

def form_eliminar_user(request,id):
    user = User.objects.get(idUser=id)
    user.delete()
    return redirect('mostrar')