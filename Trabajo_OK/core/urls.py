"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from .views import home,producto,form_update,form_create,lista_suscripcion,SuscripcionViewset
from rest_framework import routers                                 # api

router = routers.DefaultRouter()                                   # api
router.register('suscripcion', SuscripcionViewset)                       # api

urlpatterns = [
    path('', home, name="home"),
    path('producto', producto, name='producto'),
    path('form_update/<id>', form_update, name='form_update'),
    path('form_create', form_create, name='form_create'),
    path('lista_suscripcion', lista_suscripcion, name='lista_suscripcion'),
    path('api/', include(router.urls)),                            # api
]