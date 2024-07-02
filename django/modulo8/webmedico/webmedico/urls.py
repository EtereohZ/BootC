"""
URL configuration for webmedico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reserva_horas.views import vista, inicio, registro, perfil, contacto, agendar, crear_agenda, base
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista),
    path('inicio/', inicio, name="inicio"),
    path('registro/',registro, name="registro"),
    path('login/', LoginView.as_view(next_page='agendar'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('perfil/<correo>', perfil, name='perfil'),
    path('contacto/', contacto, name='contacto'),
    path('agendar/', agendar, name='agendar'),
    path('agendar/nueva', crear_agenda, name='crear_agenda'),
    path('base/', base, name='base'),
]
