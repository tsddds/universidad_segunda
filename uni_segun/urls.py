from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('convertir/', views.convertir, name='convertir'),
    path('registro/', views.register_user, name='registro'),
    path('perfil_usuario/<int:usuario_id>/', views.perfil_usuario, name='perfil_usuario'),
    path('actualizar_perfil/', views.actualizar_perfil, name='actualizar_perfil'),
    path('carrodecompra/', views.carrodecompra, name='carrodecompra'),
    path('formadepago/', views.formadepago, name='formadepago'),
    path('inicioUsuario/', views.inicioUsuario, name='inicioUsuario'),
    path('paginaProductoPrueva/<int:producto_id>', views.paginaProductoPrueva, name='paginaProductoPrueva'),
    path('comprarAhora/<int:producto_id>', views.comprarAhora, name='comprarAhora'),
    path('redireccionarte/', views.redireccioao, name='redireccionarte'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('venderProducto/', views.venderProducto, name='venderProducto'),
    path('agregar_al_carritos/<int:producto_id>/', views.agregar_al_carritos, name='agregar_al_carritos'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('disminuir_producto_offcanvas/<int:producto_id>/', views.disminuir_producto_offcanvas, name='disminuir_producto_offcanvas'),
    path('disminuir_producto/<int:producto_id>/', views.disminuir_producto, name='disminuir_producto'),
    path('aumentar_producto/<int:producto_id>/', views.aumentar_producto, name='aumentar_producto'),
    path('limpiar_del_carrito/<int:producto_id>/', views.limpiar_del_carrito, name='limpiar_del_carrito'),
    path('misproductos/', views.misproductos, name='misproductos'),
    path('eliminarProductos/<int:producto_id>', views.eliminarProductos, name='eliminarProductos'),
    path('convertir_moneda/', views.convertir_moneda, name='convertir_moneda'),
    path('editarProducto/<int:producto_id>', views.editarProducto, name='editarProducto'),
]