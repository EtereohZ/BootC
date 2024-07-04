from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Inmuebles, CustomUser
from .forms import CustomUserCreationForm, UserUpdateForm, InmuebleForm, InmuebleUpdateForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

def base(request):
    return render(request, 'base.html')


def vista(request):
    return redirect('inicio/')

def inicio(request):
    inmuebles = Inmuebles.objects.all()
    context = {
        "inmuebles" : inmuebles
    }
    return render(request, 'inicio.html', context)

def registro(request):
    if request.method == 'POST':
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inicio')

    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registro.html', {'form' : form})

@login_required(login_url="/login/")
def profile(request, correo):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado")
            return redirect("perfil", form.correo)
    user = get_user_model().objects.filter(correo=correo).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(request, 'registration/profile.html', {'form' : form})
    return redirect("inicio/")

@login_required(login_url="/login/")
def crear_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.id_usuario = request.user
            formulario.save()
            messages.success(request, 'Inmueble creado correctamente')
            return redirect("crear_inmueble")
    else:
        form = InmuebleForm()
    return render(request, 'crear_inmueble.html', {'form' : form})


class InmueblesView(ListView):
    model = Inmuebles

    def listar_inmuebles(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class InmuebleView(DetailView):
    model = Inmuebles
    template_name = 'editar_inmueble.html'
    def listar_inmueble(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context