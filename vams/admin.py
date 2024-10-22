from django.contrib import admin

# Register your models here.

from .models import Productos, Clientes, Empleados, Factura


admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Empleados)
admin.site.register(Factura)