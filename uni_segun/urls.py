# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('carrodecompra/', views.carrodecompra, name='carrodecompra'),
    path('formadepago/', views.formadepago, name='formadepago'),
    path('inicioUsuario/', views.inicioUsuario, name='inicioUsuario'),
    path('paginaProductoPrueva/', views.paginaProductoPrueva, name='paginaProductoPrueva'),
    path('login/', views.login_view, name='login'),
]
