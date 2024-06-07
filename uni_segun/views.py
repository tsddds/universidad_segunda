# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

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
       
   