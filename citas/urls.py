from django.urls import path
from .views import calendario, nueva_cita, api_citas
from django.urls import path, include


urlpatterns = [
    path('calendario/', calendario, name='calendario'),
    path('nueva/', nueva_cita, name='nueva_cita'),
    path('api/citas/', api_citas, name='api_citas'),
    path('pacientes/', include('pacientes.urls')),

]
