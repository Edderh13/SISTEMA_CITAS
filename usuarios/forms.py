from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Consultorio

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'rol', 'consultorio']
