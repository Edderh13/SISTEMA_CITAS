from django.db import models
from pacientes.models import Paciente  # ya la tienes en tu app pacientes
from django.utils import timezone



class Servicio(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre



class Membresia(models.Model):
    """
    Plantilla de membresía (ej. "Membresía Hígado Graso 8700")
    """
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class MembresiaServicio(models.Model):
    """
    Qué servicios incluye una membresía y cuántas veces.
    Ej: Membresía Hígado Graso -> 4 consultas, 6 sueros, 2 detox, etc.
    """
    membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE, related_name='servicios_incluidos')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad_incluida = models.PositiveIntegerField(
        help_text="Número de veces que se puede usar este servicio con esta membresía."
    )

    def __str__(self):
        return f"{self.membresia.nombre} - {self.servicio.nombre} x {self.cantidad_incluida}"


class MembresiaPaciente(models.Model):
    """
    Membresía que compró un paciente en una fecha.
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='membresias')
    membresia = models.ForeignKey(Membresia, on_delete=models.PROTECT)
    fecha_compra = models.DateTimeField(default=timezone.now)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.paciente.nombre} - {self.membresia.nombre}"


class UsoMembresia(models.Model):
    """
    Registro de cada vez que el paciente usa un servicio que está dentro de su membresía.
    Luego lo ligaremos con Cita.
    """
    membresia_paciente = models.ForeignKey(MembresiaPaciente, on_delete=models.CASCADE, related_name='usos')
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    fecha_uso = models.DateTimeField(default=timezone.now)
    cantidad_usada = models.PositiveIntegerField(default=1)

    # Más adelante se puede agregar: cita = models.ForeignKey('citas.Cita', ...)

    def __str__(self):
        return f"Uso {self.servicio.nombre} - {self.membresia_paciente.paciente.nombre}"
