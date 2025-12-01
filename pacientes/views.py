from django.shortcuts import render
from .models import Paciente
from django.db.models import Q

def lista_pacientes(request):

    query = request.GET.get("buscar", "")

    pacientes = Paciente.objects.all().order_by("nombre")

    if query:
        pacientes = pacientes.filter(
            Q(nombre__icontains=query) |
            Q(telefono__icontains=query)
        )

    contexto = {
        "pacientes": pacientes,
        "buscar": query
    }

    return render(request, "pacientes/lista.html", contexto)
