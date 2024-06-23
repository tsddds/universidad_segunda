from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
     path('perfil_usuario/<int:usuario_id>/', views.perfil_usuario, name='perfil_usuario'),
    path('actualizar_perfil/', views.actualizar_perfil, name='actualizar_perfil'),
    path('carrodecompra/', views.carrodecompra, name='carrodecompra'),
    path('formadepago/', views.formadepago, name='formadepago'),
    path('inicioUsuario/', views.inicioUsuario, name='inicioUsuario'),
    path('paginaProductoPrueva/', views.paginaProductoPrueva, name='paginaProductoPrueva'),
    path('login/', views.login_view, name='login'),
    path('venderProducto/', views.venderProducto, name='venderProducto'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('disminuir_producto_offcanvas/<int:producto_id>/', views.disminuir_producto_offcanvas, name='disminuir_producto_offcanvas'),
    path('disminuir_producto/<int:producto_id>/', views.disminuir_producto, name='disminuir_producto'),
    path('aumentar_producto/<int:producto_id>/', views.aumentar_producto, name='aumentar_producto'),
    path('limpiar_del_carrito/<int:producto_id>/', views.limpiar_del_carrito, name='limpiar_del_carrito'),
    path('misproductos/', views.misproductos, name='misproductos'),
]