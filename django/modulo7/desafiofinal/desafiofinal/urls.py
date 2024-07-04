
"""
URL configuration for desafiofinal project.

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
from arriendos.views import inicio, vista, base, registro, profile, crear_inmueble, InmueblesView, InmuebleView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio, name='inicio'),
    path('', vista),
    path('perfil/<correo>/', profile, name='perfil'),
    path('registro/', registro, name='registro'),
    path('login/', LoginView.as_view(next_page='inicio'), name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('crear_inmuebles/', crear_inmueble, name='crear_inmueble'),
    path('ver_inmuebles/', InmueblesView.as_view(), name='ver_inmuebles'),
    path('editar_inmueble/<pk>', InmuebleView.as_view(), name='editar_inmueble'),
    path('base', base, name='base'),
]
