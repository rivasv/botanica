from urllib import response
from django.shortcuts import render

from core.forms import ProductoForm,SuscripcionForm
from .models import Producto,Suscripcion
from rest_framework import viewsets
from .serializers import SuscripcionSerializer
from django.utils.decorators import method_decorator  #
from django.views.decorators.csrf import csrf_exempt  #


class SuscripcionViewset(viewsets.ModelViewSet):

#    @method_decorator(csrf_exempt)
#    def dispatch(self, request, *args, **kwargs):          #
#        return super().dispatch(request, *args, **kwargs)  #
#
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer                #clase que los serializa lleva a json
 
    # http://127.0.0.1:8000/api/suscripcion                        <- listado completo
    # http://127.0.0.1:8000/api/suscripcion/?accion=c&rut=2   <- consulta un caso
    # Solo entra aqui cuando viene parametro via urls

    def get_queryset(self):
        suscripcion = Suscripcion.objects.all()
        parrut = self.request.GET.get('rut')              # trae todas las var de la url y recupero rut

        if ( parrut ):
           suscripcion = suscripcion.filter(rut=parrut)   # filtro rut recuperado
        return suscripcion

        if self.request.method == "DELETE":
           suscripcion.delete()
        return Response("eliminado")           


# para que llame a /templates/core
def lista_suscripcion(request):
    return render(request, 'core/lista_suscripcion.html')

    
def home(request):
    return render(request, 'core/home.html')

def producto (request):
    productos = Producto.objects.all()
    datos = {
        'producto' : productos
    }
    return render (request, 'core/producto.html', datos)

def form_update(request, id):
    producto = Producto.objects.get(codigo = id)

    datos = {
         'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
       formulario = ProductoForm(request.POST,instance=producto)
       if formulario.is_valid:
          formulario.save()
          datos['mensaje'] = "actualizado correctamente!"

    return render(request, 'core/form_update.html', datos)

def form_create(request):
    datos = {
         'form' : ProductoForm()
    }

    if request.method == 'POST':
       formulario = ProductoForm(request.POST)
       if formulario.is_valid:
          formulario.save()
          datos['mensaje'] = "guardado correctamente!"
    return render(request, 'core/form_create.html', datos)