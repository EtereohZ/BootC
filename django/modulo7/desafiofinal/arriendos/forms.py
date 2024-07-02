from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser, Inmuebles, Regiones, Comunas


class CustomUserCreationForm(UserCreationForm):
    rut = forms.CharField(label='RUT')
    nombre = forms.CharField(label='Nombres', max_length=30)
    apellido = forms.CharField(label='Apellidos', max_length=30)
    correo = forms.CharField(label='Correo electrónico', max_length=50)
    direccion = forms.CharField(label='Dirección', max_length=80)
    telefono = forms.CharField(label='Telefono')
    tipo_usuario = forms.ChoiceField(choices=CustomUser.TipoUsuario.choices)
    password1 = forms.CharField(label='Contraseña',
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña',
        widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["rut", "nombre", "apellido", "correo", "direccion", "telefono", "tipo_usuario"]

    def clean_correo(self):
        #Valida que el correo ingresado no este en la BD
        correo = self.cleaned_data.get('correo')
        if CustomUser.objects.filter(correo = correo).exists():
            raise ValidationError("Correo ya existe")
        else:
            return self.data['correo']

    def clean_rut(self):
        #Valida que el rut ingresado no este en la BD
        rut = self.cleaned_data.get('rut')
        if CustomUser.objects.filter(rut = rut).exists():
            raise forms.ValidationError("RUT ya registrado")
        else:
            return self.data['rut']
        
    def clean_password2(self):
        #Validador para asegurarse que la contraseña ingresada sea la deseada
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2') 
        if password1 != password2:
            raise ValidationError("Las contraseñas no son iguales")
        else:
            return self.data['password2']
        
class UserUpdateForm(forms.ModelForm):
    correo = forms.CharField(label="Correo", max_length=50)

    class Meta:
        model = get_user_model()
        fields = ['rut', 'nombre', 'apellido', 'correo', 'direccion', 'telefono']

class InmuebleForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre del inmueble', max_length=50)
    descripcion = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'cols' : 50}))
    m2_construidos = forms.CharField(label='m2 Construidos', max_length=10)
    m2_totales = forms.CharField(label='m2 Totales', max_length=10)
    cantidad_estacionamientos = forms.CharField(label='Numero de estacionamientos')
    cantidad_habitaciones = forms.CharField(label='Numero de habitaciones')
    cantidad_baños = forms.CharField(label='Baños')
    direccion = forms.CharField(label='Dirección', max_length=30)
    region = forms.ChoiceField(label='Región', choices=Regiones.choices)
    comuna = forms.ChoiceField(label='comuna', choices=Comunas.choices)
    tipo_inmueble = forms.ChoiceField(label='Tipo de inmueble', choices=Inmuebles.TipoInmueble.choices)
    precio_mensual = forms.CharField(label='precio')

    class Meta():
        model = Inmuebles
        fields = ['nombre', 'descripcion', 'm2_construidos', 'm2_totales', 'cantidad_estacionamientos', 'cantidad_habitaciones', 'cantidad_baños', 'direccion', 'region', 'comuna', 'tipo_inmueble', 'precio_mensual']

class InmuebleUpdateForm(forms.ModelForm):

    class Meta:
        model = Inmuebles
        fields = '__all__'
    