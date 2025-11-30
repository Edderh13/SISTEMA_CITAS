from django.contrib import admin
from django.urls import path, include
from usuarios.views import login_view  # 👈 importamos nuestra vista
# ya no necesitamos importar dashboard aquí si no lo usaremos como home

urlpatterns = [
    # Si quieres que la raíz mande al calendario:
    path('', lambda request: redirect('/citas/calendario/')),

    path('admin/', admin.site.urls),

    path('citas/', include('citas.urls')),
    path('usuarios/', include('usuarios.urls')),

    path('login/', login_view, name='login'),
    path('logout/', include('django.contrib.auth.urls')),  # o dejas tu logout actual si ya funciona
]
