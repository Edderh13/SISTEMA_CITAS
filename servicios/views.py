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

    return render(request, 'servicios/form.html', {
        'form': form,
        'titulo': 'Nuevo Servicio'
    })

@login_required
def editar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)

    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm(instance=servicio)

    return render(request, 'servicios/form.html', {
        'form': form,
        'titulo': 'Editar Servicio'
    })

@login_required
def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    return redirect('lista_servicios')
