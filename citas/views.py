from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Cita


# ============================
#   DASHBOARD (si lo usas)
# ============================
@login_required
def dashboard(request):
    """
    Vista simple de dashboard (por ahora no usamos mucho).
    """
    return render(request, 'dashboard.html')


# ============================
#   CALENDARIO PRINCIPAL
# ============================
@login_required
def calendario(request):
    """
    Vista principal del calendario de citas.
    """
    return render(request, 'calendario.html')


# ============================
#   API DEL CALENDARIO
#   (Carga citas desde la BD)
# ============================
@login_required
def api_citas(request):
    """
    Devuelve las citas en formato JSON para FullCalendar.
    """
    citas = Cita.objects.all()
    data = []

    for c in citas:
        data.append({
            "id": c.id,
            "title": f"{c.nutriologa} | {c.servicio}",
            "start": f"{c.fecha}T{c.hora_inicio}",
            "end": f"{c.fecha}T{c.hora_fin}",
            "color": "#4ab4f9",  # luego ponemos color por nutrióloga
        })

    return JsonResponse(data, safe=False)


# ============================
#   CREAR NUEVA CITA (POST)
# ============================
@login_required
def nueva_cita(request):
    """
    Recibe el formulario de 'Nueva cita' del modal y guarda en la BD.
    Luego regresa al calendario.
    """
    if request.method == "POST":
        paciente = request.POST.get("paciente")
        nutriologa = request.POST.get("nutriologa")
        servicio = request.POST.get("servicio")
        fecha = request.POST.get("fecha")
        hora_inicio = request.POST.get("hora_inicio")
        hora_fin = request.POST.get("hora_fin")
        notas = request.POST.get("notas")

        if paciente and nutriologa and servicio and fecha and hora_inicio and hora_fin:
            Cita.objects.create(
                paciente=paciente,
                nutriologa=nutriologa,
                servicio=servicio,
                fecha=fecha,
                hora_inicio=hora_inicio,
                hora_fin=hora_fin,
                notas=notas or "",
            )

    # Siempre regresamos al calendario
    return redirect("calendario")
