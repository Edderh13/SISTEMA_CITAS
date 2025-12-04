# sistema_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from usuarios.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login
    path('login/', login_view, name='login'),

    # Al entrar a "/" te mando al login
    path('', lambda request: redirect('login')),

    # Apps
    path('citas/', include('citas.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('servicios/', include('servicios.urls')),
    path('usuarios/', include('usuarios.urls')),
]
