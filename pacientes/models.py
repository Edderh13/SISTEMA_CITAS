from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField(null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
