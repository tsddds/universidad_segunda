from django.contrib import admin
from .models import CategoriaProducto, Producto, Usuario, CarroCompra, Tarjetas, Direcciones


admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(CarroCompra)
admin.site.register(Tarjetas)
admin.site.register(Direcciones)
