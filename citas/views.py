from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Cita


# ============================
#   DASHBOARD (POR SI LO USAS)
# ============================
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# ============================
#   CALENDARIO
# ============================
@login_required
def calendario(request):
    return render(request, 'calendario.html')


# ============================
#   API PARA CARGAR CITAS
# ============================
def api_citas(request):
    citas = Cita.objects.all()
    data = []

    for c in citas:
        data.append({
            "id": c.id,
            "title": f"{c.nutriologa} | {c.servicio}",
            "start": f"{c.fecha}T{c.hora_inicio}",
            "end": f"{c.fecha}T{c.hora_fin}",
            "color": "#4ab4f9",
        })

    return JsonResponse(data, safe=False)


# ============================
#   FORMULARIO NUEVA CITA
# ============================
@login_required
def nueva_cita(request):
    from .forms import CitaForm

    form = CitaForm()
    return render(request, "nueva_cita.html", {"form": form})


# ============================
#   API PARA CREAR CITAS (POST)
# ============================
@csrf_exempt
@login_required
def api_crear_cita(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        cita = Cita.objects.create(
            nutriologa=data.get("nutriologa"),
            paciente=data.get("paciente"),
            servicio=data.get("servicio"),
            fecha=data.get("fecha"),
            hora_inicio=data.get("hora_inicio"),
            hora_fin=data.get("hora_fin"),
            notas=data.get("notas", "")
        )

        return JsonResponse({
            "status": "ok",
            "id": cita.id,
            "title": f"{cita.nutriologa} | {cita.servicio}",
            "start": f"{cita.fecha}T{cita.hora_inicio}",
            "end": f"{cita.fecha}T{cita.hora_fin}",
        })

    return JsonResponse({"error": "Método no permitido"}, status=405)

