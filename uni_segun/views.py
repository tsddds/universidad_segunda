# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Direcciones, Usuario, Producto, CategoriaProducto
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def index(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'index.html', context)

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

def aumentar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', [])
    
    for item in carrito:
        if item['id'] == producto.id:
            item['cantidad'] += 1
            break
    request.session['carrito'] = carrito
    return redirect('carrodecompra')

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


def limpiar_del_carrito(request,producto_id):
    carrito = request.session.get('carrito', [])
    for item in carrito:
        if item['id'] == producto_id:
            carrito.remove(item)
            request.session['carrito'] = carrito
    return redirect('carrodecompra')

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

def formadepago(request):
    carrito = request.session.get('carrito', [])
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    context = {
        'total': total,
        
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

def paginaProductoPrueva(request):
    return render(request, 'paginaProductoPrueva.html')

def login_view(request):
    return redirect('inicioUsuario')



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