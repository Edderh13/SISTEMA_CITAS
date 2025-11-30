from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from usuarios.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # login
    path('login/', login_view, name='login'),

    # redirección del root
    path('', lambda request: redirect('/citas/calendario/')),

    # apps
    path('usuarios/', include('usuarios.urls')),
    path('citas/', include('citas.urls')),
    path('admin/', admin.site.urls),
]
