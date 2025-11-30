from django.urls import path
from .views import login_view   # 🔥 ya NO importamos registrar_usuario

urlpatterns = [
    path('login/', login_view, name='login'),
]
