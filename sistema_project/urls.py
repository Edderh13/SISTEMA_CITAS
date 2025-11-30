from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from usuarios.views import login_view

urlpatterns = [
    # ruta principal → redirige al login
    path('', lambda request: redirect('/login/')),

    # login
    path('login/', login_view, name='login'),

    # apps
    path('usuarios/', include('usuarios.urls')),
    path('citas/', include('citas.urls')),

    # admin
    path('admin/', admin.site.urls),
]
