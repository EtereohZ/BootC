
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    rut = forms.CharField(label='RUT')
    nombre = forms.CharField(label='Nombres', max_length=30)
    apellido = forms.CharField(label='Apellidos', max_length=30)
    correo = forms.CharField(label='Correo electrónico', min_length=5, max_length=50)
    direccion = forms.CharField(label='Dirección', max_length=80)
    telefono = forms.CharField(label='Telefono')
    tipo_usuario = forms.ChoiceField(choices=CustomUser.TipoUsuario.choices)
    password1 = forms.CharField(label='Contraseña',
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña',
        widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["rut", "nombre", "apellido", "correo", "direccion", "telefono", "tipo_usuario", "password1"]

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
