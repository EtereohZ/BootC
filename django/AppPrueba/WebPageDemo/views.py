from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("""
   <h1>Bienvenidos a *NombreNoDisponible*</h1>
   <h2>Su mejor recurso para soluciones *SolucionesNoDeterminadas*</h2>
   <h3>Confíe en nuestros () para poder lograr sus ()</h3>
""")
    

def about(request):
    return HttpResponse("""
    <h1>Sobre nosotros</h1>
    <p>
        Nuestra larga trayectoria inicia en el año 2024 por la visión y el cuidado del gran maestro *InsertarNombreDirectorActual*.<br>
        Somos una compañia honesta con un ideal incorrompible* que nos guía a formar un futuro mejor.<br>
        Consulta con nuestros embajadores para mayor información.<br>
        <br>

        *información sujeta a cambios.
    </p>
""")


def contact(request):
    return HttpResponse("""
    <h1>Contacto</h1>
    <h4>Garantizamos un sello de calidad sin igual.
        Nuestros operadores se comprometen a responder dentro de un plazo minimo de: 5 semanas y 3 días.</h4>
    <p>
    <form action="">
        <label for="name">Nombre Completo:</label><br>
        <input type="text" id="name"><br>
        <label for="comment">Escribenos:</label><br>
        <input type="text" id="comment">

    </form>
                                               
""")