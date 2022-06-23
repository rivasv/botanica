from dataclasses import fields
from pyexpat import model
from django import forms
from django import forms
from django.forms import ModelForm
from .models import Producto,Suscripcion, Categoria

class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        fields = ['codigo','nombre','precio','stock','categoria']

class SuscripcionForm(ModelForm):
    class Meta:
        model= Suscripcion
        fields = ['id','rut','estado']