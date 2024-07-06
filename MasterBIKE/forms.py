from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario 


class UsuarioRegisterForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email']