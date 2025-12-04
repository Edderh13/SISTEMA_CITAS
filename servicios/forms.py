# servicios/forms.py
from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio', 'duracion', 'activo']
        labels = {
            'nombre': 'Nombre del servicio',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'duracion': 'Duración (minutos)',
            'activo': 'Activo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Consulta de hígado graso'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Detalles del servicio'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'duracion': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '5'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
