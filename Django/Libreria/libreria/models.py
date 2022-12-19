from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Imagen')
    descripcion = models.TextField(null=True, verbose_name='Descripcion')

    def __str__ (self):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion: " + self.descripcion
        return fila 

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image

    def __str__(self):
        return f'Perfil de {self.user.username}'

