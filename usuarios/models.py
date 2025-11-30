from django.contrib.auth.models import AbstractUser
from django.db import models

class Consultorio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Usuario(AbstractUser):

    ROLES = (
        ('admin', 'Administrador'),
        ('gerente', 'Gerente'),
        ('nutriologa', 'Nutrióloga'),
    )

    rol = models.CharField(max_length=20, choices=ROLES)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.SET_NULL,
                                    null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
