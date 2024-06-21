from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + ' ' + self.apellido