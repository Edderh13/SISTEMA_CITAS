from django.db import models

class Cita(models.Model):
    paciente = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    sucursal = models.CharField(max_length=100)
    nutriologa = models.CharField(max_length=100)
    servicio = models.CharField(max_length=200)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente} - {self.servicio}"
