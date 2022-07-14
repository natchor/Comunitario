from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class User(models.Model):
    idUser = models.CharField(primary_key=True,verbose_name="ID USER" )
    nombreUser = models.CharField(max_length=50, verbose_name="Nombre USER")
    correo = models.CharField(max_length=50, verbose_name="Correo User")
    password = models.AutoField(max_length=10, verbose_name="Password")
    nac= models.DateField(verbose_name="Fecha Nacimiento")

    def __str__(self):

        return (self.idUser)

class Vehiculo(models.Model):

    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca')
    modelo = models.CharField(max_length=20, verbose_name='Modelo')
    categoria = models.ForeignKey(User, on_delete=CASCADE)



    def __str__(self):

        return (self.patente)