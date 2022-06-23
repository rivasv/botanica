from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id')
    nombreCategoria = models.CharField(max_length=30, verbose_name='Nombre C')
    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    codigo = models.CharField(max_length=5,primary_key=True,verbose_name='Codigo ')
    nombre = models.CharField(max_length=30,verbose_name='Nombre producto')
    precio = models.CharField(max_length=15,verbose_name='Precio $')
    stock = models.CharField(max_length=25,default='',verbose_name='Stock: ')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.codigo

class Suscripcion(models.Model):
    rut = models.CharField(max_length=10,verbose_name='Rut del socio')
    estado = models.CharField(max_length=1,verbose_name='Estado vigencia')
    def __str__(self):
        return self.rut

