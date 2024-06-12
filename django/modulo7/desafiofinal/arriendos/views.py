from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Inmuebles, CustomUser
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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