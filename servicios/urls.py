from django.urls import path
from .views import lista_servicios, nuevo_servicio, editar_servicio, eliminar_servicio

urlpatterns = [
    path('', lista_servicios, name='lista_servicios'),
    path('nuevo/', nuevo_servicio, name='nuevo_servicio'),
    path('editar/<int:id>/', editar_servicio, name='editar_servicio'),
    path('eliminar/<int:id>/', eliminar_servicio, name='eliminar_servicio'),
]
