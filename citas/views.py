from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Cita


# ============================
#   DASHBOARD (ya lo tenías)
# ============================
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# ============================
#   CALENDARIO PRINCIPAL
# ============================
@login_required
def calendario(request):
    return render(request, 'calendario.html')


# ============================
#   API DEL CALENDARIO
#   (Carga citas desde la BD)
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
            "color": "#4ab4f9"  # más adelante pondremos color por nutrióloga
        })

    return JsonResponse(data, safe=False)
