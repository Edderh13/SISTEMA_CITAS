# servicios/models.py
from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
