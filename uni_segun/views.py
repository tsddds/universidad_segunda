# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def carrodecompra(request):
    return render(request, 'carrodecompra.html')

def formadepago(request):
    return render(request, 'formadepago.html')

def inicioUsuario(request):
    return render(request, 'inicioUsuario.html')

def paginaProductoPrueva(request):
    return render(request, 'paginaProductoPrueva.html')

def login_view(request):
    return redirect('inicioUsuario')

def AgregarCarro(request):
    nombre = request.POST['']
    descripcion =  request.POST['']
    precio =  request.POST['']
    categoria = request.POST['']

    return render(request, 'inicioUsuario.html')
       
def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        rut = request.POST['rut']
        academia = request.POST['academia']
        email = request.POST['email']
        contraseña = request.POST['contraseña']
        numero_de_telefono = request.POST['numero_de_telefono']

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado.')
        elif Usuario.objects.filter(rut=rut).exists():
            messages.error(request, 'El RUT ya está registrado.')
        elif Usuario.objects.filter(numero_de_telefono=numero_de_telefono).exists():
            messages.error(request, 'El número de teléfono ya está registrado.')
        else:
            usuario = Usuario(
                nombre=nombre,
                apellido=apellido,
                rut=rut,
                academia=academia,
                email=email,
                contraseña=contraseña,
                numero_de_telefono=numero_de_telefono
            )
            usuario.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('inicioUsuario')

    return render(request, 'registro.html')