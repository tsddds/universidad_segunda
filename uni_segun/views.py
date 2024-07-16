# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
import requests
from .models import Direcciones, Usuario, Producto, CategoriaProducto
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def obtener_tasa_cambio():
    url = f"https://v6.exchangerate-api.com/v6/{settings.EXCHANGE_RATE_API_KEY}/latest/CLP"
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']['USD']

def convertir_moneda(request):
    tasa_cambio = obtener_tasa_cambio()
    dolares = None
    pesos_chilenos = None

    if request.method == 'POST':
        pesos_chilenos = float(request.POST.get('pesos_chilenos'))
        dolares = pesos_chilenos * tasa_cambio

    context = {
        'tasa_cambio': tasa_cambio,
        'pesos_chilenos': pesos_chilenos,
        'dolares': dolares,
    }
    return render(request, 'convertir_moneda.html', context)

def convertir(request):
    carrito = request.session.get('carrito', [])
    return redirect('convertir_moneda')

def index(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'index.html', context)

@login_required
def perfil_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    cant = sum(item['cantidad'] for item in carrito)
    context = {
        'carrito': carrito,
        'total': total,
        'cant':cant,
        'usuario': usuario,
        
        
    }
    return render(request, 'perfil.html', context)

@login_required
def actualizar_perfil(request):
      if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        usuario = get_object_or_404(Usuario, id=usuario_id)
        usuario.nombre = request.POST.get('nombre')
        usuario.apellido = request.POST.get('apellido')
        usuario.academia = request.POST.get('academia')
        usuario.email = request.POST.get('email')
        usuario.numero_de_telefono = request.POST.get('numero_de_telefono')
        usuario.save()
        

        messages.success(request, 'Perfil actualizado exitosamente.')
        return redirect('perfil_usuario', usuario_id=usuario.id)
 
@login_required
def carrodecompra(request):
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    cant = sum(item['cantidad'] for item in carrito)
    context = {
        'carrito': carrito,
        'total': total,
        'cant':cant
    }
    return render(request, 'carrodecompra.html', context)
    
@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', [])
    
    for item in carrito:
        if item['id'] == producto.id:
            item['cantidad'] += 1
            break
    else:
        carrito.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion':producto.descripcion,
            'precio': float(producto.precio),  
            'cantidad': 1,
            'imagen': producto.imagen.url if producto.imagen else None
        })
    
    request.session['carrito'] = carrito
    return redirect('inicioUsuario')

@login_required
def agregar_al_carritos(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', [])
    
    for item in carrito:
        if item['id'] == producto.id:
            item['cantidad'] += 1
            break
    else:
        carrito.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion':producto.descripcion,
            'precio': float(producto.precio),  
            'cantidad': 1,
            'imagen': producto.imagen.url if producto.imagen else None
        })
    
    request.session['carrito'] = carrito
    return redirect(reverse('paginaProductoPrueva', args=[producto_id]))

@login_required
def comprarAhora(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', [])
    
    for item in carrito:
        if item['id'] == producto.id:
            item['cantidad'] += 1
            break
    else:
        carrito.append({
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion':producto.descripcion,
            'precio': float(producto.precio),  
            'cantidad': 1,
            'imagen': producto.imagen.url if producto.imagen else None
        })
    
    request.session['carrito'] = carrito
    return redirect('carrodecompra')

@login_required
def aumentar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', [])
    
    for item in carrito:
        if item['id'] == producto.id:
            item['cantidad'] += 1
            break
    request.session['carrito'] = carrito
    return redirect('carrodecompra')

@login_required
def disminuir_producto(request, producto_id):
    carrito = request.session.get('carrito', [])
    for item in carrito:
        if item['id'] == producto_id:
            item['cantidad'] -= 1
            if item['cantidad'] <= 0:
                carrito.remove(item)
            break
    request.session['carrito'] = carrito
    return redirect('carrodecompra')

@login_required
def disminuir_producto_offcanvas(request, producto_id):
    carrito = request.session.get('carrito', [])
    for item in carrito:
        if item['id'] == producto_id:
            item['cantidad'] -= 1
            if item['cantidad'] <= 0:
                carrito.remove(item)
            break
    request.session['carrito'] = carrito
    return redirect('inicioUsuario')

@login_required
def limpiar_del_carrito(request,producto_id):
    carrito = request.session.get('carrito', [])
    for item in carrito:
        if item['id'] == producto_id:
            carrito.remove(item)
            request.session['carrito'] = carrito
    return redirect('carrodecompra')

@login_required
def venderProducto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria_id = request.POST['categoria']
        imagen = request.FILES['imagen']

        try:
            categoria = CategoriaProducto.objects.get(id=categoria_id)
        except CategoriaProducto.DoesNotExist:
            messages.error(request, 'La categoría seleccionada no existe.')
            return redirect('venderProducto')

        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria,
            imagen=imagen  # Let Django handle the file upload
        )
        producto.save()

        messages.success(request, 'Producto publicado exitosamente.')
        return redirect('inicioUsuario')

    return render(request, 'venderProducto.html')

@login_required
def formadepago(request):
    usuarios = Usuario.objects.all() 
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    context = {
        'total': total,
        'usuarios':usuarios
        
    }
    return render(request, 'formadepago.html', context)

def inicioUsuario(request):    
    usuarios = Usuario.objects.all() 
    productos = Producto.objects.all()
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    cant = sum(item['cantidad'] for item in carrito)
    context = {
        'carrito': carrito,
        'total': total,
        'cant':cant,
        'productos': productos,
        'usuarios':usuarios
    }
    return render(request, 'inicioUsuario.html', context)

# para enviar al usuario al index 
def redireccioao(request):
    messages.success(request, ("No has iniciado sesión..."))
    return render(request, 'redireccionarte.html')

# para loguear al usuario
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "¡¡Ha iniciado sesión!! uwu")
                return redirect('inicioUsuario')
            else:
                messages.error(request, "Ups.. esa no parece ser su contraseña o su usuario... intentelo nuevamente")
                return redirect('index')
        else:
            messages.error(request, "Ups.. esa no parece ser su contraseña o su usuario... intentelo nuevamente")
            return redirect('index')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

#cuando el usuario termina su sesión
def logout_user(request):
    logout(request)
    messages.success(request, ("ha terminado su sesión... gracias por su estancia"))
    return redirect('index')

@login_required
def paginaProductoPrueva(request):
    usuarios = Usuario.objects.all() 
    productos = Producto.objects.all()
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    cant = sum(item['cantidad'] for item in carrito)
    context = {
        'carrito': carrito,
        'total': total,
        'cant':cant,
        'productos': productos,
        'usuarios':usuarios
    }
    return render(request, 'paginaProductoPrueva.html')


#para registar usuario
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Aquí logueamos al usuario
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Ha sido registrado exitosamente.")
                return redirect('inicioUsuario')
            else:
                messages.error(request, "Autenticación fallida. Por favor, intente iniciar sesión.")
                return redirect('login')
        else:
            messages.error(request, "Error al registrar, inténtelo nuevamente")
            return render(request, 'registro.html', {'form': form})
    else:
        return render(request, 'registro.html', {'form': form})

@login_required
def misproductos(request):
    usuarios = Usuario.objects.all() 
    productos = Producto.objects.all()
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    cant = sum(item['cantidad'] for item in carrito)
    context = {
        'carrito': carrito,
        'total': total,
        'cant':cant,
        'productos': productos,
        'usuarios':usuarios
    }
    return render(request, 'misproductos.html', context)

@login_required
def eliminarProductos(request, producto_id):
    usuarios = Usuario.objects.all() 
    productos = Producto.objects.all()
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    cant = sum(item['cantidad'] for item in carrito)
    context = {
        'carrito': carrito,
        'total': total,
        'cant':cant,
        'productos': productos,
        'usuarios':usuarios
    }
    producto = Producto.objects.get(id=producto_id)
    producto.delete()

    return render(request, 'misproductos.html',context)

@login_required
def paginaProductoPrueva(request, producto_id):
    productovista = Producto.objects.get(id=producto_id)
    usuarios = Usuario.objects.all() 
    productos = Producto.objects.all()
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    cant = sum(item['cantidad'] for item in carrito)
    contexto = {
        'carrito': carrito,
        'total': total,
        'cant':cant,
        'usuarios':usuarios,
        'productos': productos,
        "producto":productovista
    }
    
    return render(request, 'paginaProductoPrueva.html',contexto)

@login_required
def editarProducto(request, producto_id):
     if request.method == 'GET':
        productovista = Producto.objects.get(id=producto_id)
        usuarios = Usuario.objects.all() 
        productos = Producto.objects.all()
        carrito = request.session.get('carrito', [])
        total = sum(item['precio'] * item['cantidad'] for item in carrito)
        cant = sum(item['cantidad'] for item in carrito)
        contexto = {
            'carrito': carrito,
            'total': total,
            'cant':cant,
            'usuarios':usuarios,
            'productos': productos,
            "producto":productovista
        }
        return render(request, 'editarProducto.html',contexto)
     
     if request.method == 'POST':
        producto = Producto.objects.get(id=producto_id)
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria_id = request.POST['categoria']
        imagen = request.FILES['imagen']

        try:
            categoria = CategoriaProducto.objects.get(id=categoria_id)
        except CategoriaProducto.DoesNotExist:
            messages.error(request, 'La categoría seleccionada no existe.')
            return redirect('editarProducto')

        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.categoria = categoria
        producto.imagen = imagen
        producto.save()

        return redirect("/misproductos/")