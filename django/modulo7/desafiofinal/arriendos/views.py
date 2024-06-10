from django.shortcuts import render, redirect, HttpResponseRedirect, get_list_or_404
from .models import Inmuebles, CustomUser
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/inicio')
        messages.success(request, 'Cuenta creada correctamente')

    else:
        form = CustomUserCreationForm()
        context = {'form' : form}
    return render(request, 'registration/registro.html', context)

@login_required
def profile(request, pk):
    usuario = get_list_or_404(CustomUser, id=pk)
    
    context = {}
    return render(request, 'profile.html', context)
    pass

@login_required
def register_profile(request):
    pass