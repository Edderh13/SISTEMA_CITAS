from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import RegistroUsuarioForm


def login_view(request):
    # Obtener el "next" si venías de una página protegida
    next_url = request.GET.get('next') or request.POST.get('next') or '/citas/calendario/'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(next_url)  # 🔥 manda al calendario (o a next si venía de otra vista)

        # Si falla, mandamos un mensaje simple
        return render(request, 'login.html', {
            'error': 'Usuario o contraseña incorrectos',
        })

    # GET: solo mostrar el formulario
    return render(request, 'login.html', {'next': next_url})


def es_admin(usuario):
    return usuario.is_authenticated and usuario.rol == 'admin'


@login_required
@user_passes_test(es_admin)
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # aquí luego podemos mandar a un listado de usuarios
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})
