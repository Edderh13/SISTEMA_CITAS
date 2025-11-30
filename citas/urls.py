from django.urls import path
from .views import dashboard
from .views import calendario
from .views import calendario, api_citas   # ← ESTA LÍNEA ES LA IMPORTANTE

urlpatterns = [
    
    path('calendario/', calendario, name='calendario'),
    path("api/citas/", api_citas, name="api_citas"),
    path('nueva/', nueva_cita, name='nueva_cita'),
    path('api/crear/', api_crear_cita, name='api_crear_cita'),


]
