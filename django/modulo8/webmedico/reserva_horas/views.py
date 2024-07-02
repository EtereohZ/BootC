from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, ContactDataForm, UserUpdateForm, AgendarForm
from .models import Agenda, CustomUser
from django.contrib import messages
# Create your views here.

def base(request):
    usuarios = CustomUser.obects.all()
    context = {
        "usuarios" : usuarios
    }
    return render(request, 'base.html', context)


def vista(request):
    # Redirigimos a la pagina de inicio
    return redirect('inicio/')

def inicio(request):
    return render(request, 'inicio.html')

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
                # En esta paso la creación del usuario es exitosa, claramente
            messages.success(request, "Cuenta creada exitosamente")
            return HttpResponseRedirect('/inicio')

    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registro.html', {'form' : form})

@login_required(login_url="/login/") #este decorados solo pemite el ingreso a esa vista si está logeado, de lo contrario redirige a login
def perfil(request, correo):
    # En esta vista manejamos el perfil del usuario como la actualización de sus datos
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            # Si el formulario es válido
            user_form = form.save()
                # Se guarda
            messages.success(request, "Usuario actualizado correctamente")
            return redirect("perfil", user_form.correo)
    user = get_user_model().objects.filter(correo=correo).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(request, 'registration/profile.html', {'form' : form})
    return redirect("inicio/")

def contacto(request):
    if request.method == 'POST':
        form = ContactDataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inicio')
    else:
        form = ContactDataForm()
    return render(request, 'contacto.html', {'form' : form})

@login_required(login_url="/login/")
def agendar(request):
    agendas = Agenda.objects.all()
    context = {
        "agendas" : agendas
    }
    return render(request, 'agendar.html', context)

@login_required(login_url="/login/")
def crear_agenda(request):
    if request.method == 'POST':
        form = AgendarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Agenda creada correctamente")
            return redirect("agendar")
    else:
        form = AgendarForm()
    return render(request, 'agendador.html', {'form' : form})

