from django.shortcuts import render
from .models import Flan, ContactForm
from .forms import ContactDataForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def inicio(request):
    # flanes = Flan.objects.all()  #Con esto mostramos todos los objetos flan
    flanes_publicos = Flan.objects.filter(is_private=False)   #Con esto podemos filtrar si queremos que se muestre solo los objetos privados o publicos
    context = {
        "flanes" : flanes_publicos
    }
    return render(request, 'index.html', context) #El 'context' se tiene que pasar en el return

def acerca(request):
    return render(request, 'about.html')

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        "flanes" : flanes_privados
    }
    return render(request, 'welcome.html', context)

def contacto(request):
    if request.method == 'POST':
        #creamos el formulario y lo llenamos con la informacion
        form = ContactDataForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        #Si es cualquier otro metodo, el form quedará en blanco
        form = ContactDataForm()
    return render(request, 'contact.html', {'form' : form})

def exito(request):
    return render(request, 'success.html')

def base(request):
    return render(request, 'base.html')