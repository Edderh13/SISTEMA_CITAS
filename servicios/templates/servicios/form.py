from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio', 'duracion', 'activo']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del servicio'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del servicio (opcional)'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'duracion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minutos',
                'min': '1'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
