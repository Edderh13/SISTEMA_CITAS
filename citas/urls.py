from django.urls import path
from .views import dashboard
from .views import calendario
from .views import calendario, api_citas   # ← ESTA LÍNEA ES LA IMPORTANTE

urlpatterns = [
    
    path('calendario/', calendario, name='calendario'),
    path("api/citas/", api_citas, name="api_citas"),

]
