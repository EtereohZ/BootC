from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser, ContactForm, Agenda

class CustomUserCreationForm(UserCreationForm):
    ###Formulario manual para poder crear un usuario###
    nombre = forms.CharField(label='Nombres', max_length=30)
    apellido = forms.CharField(label='Apellidos', max_length=30)
    correo = forms.CharField(label='Correo electrónico', max_length=50)
    password1 = forms.CharField(label='Contraseña',
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña',
        widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [ "nombre", "apellido", "correo"]

    def clean_correo(self):
        # Valida que el correo ingresado no este en la BD
        correo = self.cleaned_data.get('correo')
        if CustomUser.objects.filter(correo = correo).exists():
            raise ValidationError("Correo ya existe")
        else:
            return self.data['correo']
        
    def clean_password2(self):
        # Validador para asegurarse que la contraseña ingresada sea la deseada
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2') 
        if password1 != password2:
            raise ValidationError("Las contraseñas no son iguales")
        else:
            return self.data['password2']
        
class UserUpdateForm(forms.ModelForm):
    ###Formulario para cambiar datos de usuario en el perfil###
    correo = forms.EmailField()
    class Meta:
        model = get_user_model()
        fields = ['nombre', 'apellido', 'correo']


class ContactDataForm(forms.ModelForm):
    ###Formulario para contacto###
    correo = forms.EmailField(label='Correo')
    nombre = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'cols':50}))
    correo.widget.attrs.update(size='50')
    nombre.widget.attrs.update(size='50')

    class Meta:
        model = ContactForm
        fields = ['nombre', 'correo', 'message']

class AgendarForm(forms.ModelForm):
    ###Formulario para agendar hora###
    class Meta():
        model = Agenda
        fields =['fecha_disponible', 'hora_disponible', 'especialista_id', 'centro_medico_id']
        widgets = {
            'fecha_disponible' : forms.DateInput(attrs={'type' : 'date'}),
            'hora_disponible' : forms.TimeInput(attrs={'type' : 'time'})
        }
