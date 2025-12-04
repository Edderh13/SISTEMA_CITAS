# servicios/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Servicio
from .forms import ServicioForm

@login_required
def lista_servicios(request):
    servicios = Servicio.objects.all().order_by('nombre')
    return render(request, 'servicios/lista.html', {'servicios': servicios})

@login_required
def nuevo_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm()

    return render(request, 'servicios/nuevo.html', {'form': form})

@login_required
def editar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)

    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm(instance=servicio)

    return render(request, 'servicios/nuevo.html', {
        'form': form,
        'editando': True,
        'servicio': servicio
    })

@login_required
def eliminar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)

    if request.method == 'POST':
        servicio.delete()
        return redirect('lista_servicios')

    # Si quieres, aquí podríamos mandar a una pantalla de confirmación.
    # De momento, lo borramos directo con POST.
    return redirect('lista_servicios')
