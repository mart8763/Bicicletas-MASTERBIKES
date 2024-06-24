from django.contrib import admin
from .models import Usuario, Genero, Alumno

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Genero)
admin.site.register(Alumno)