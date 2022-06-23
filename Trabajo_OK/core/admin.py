from calendar import c
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Producto)
admin.site.register(Suscripcion)
admin.site.register(Categoria)

# poto