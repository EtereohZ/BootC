
from django.urls import path
from arriendos.views import inicio, vista, base, registro, profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('', vista),
    path('perfil/<correo>/', profile, name='perfil'),
    path('registro/', registro, name='registro'),
    path('login/', LoginView.as_view(next_page='inicio'), name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('base', base, name='base'),
]
