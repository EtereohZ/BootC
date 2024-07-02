from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager
import uuid

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Models manual para crear un usuario,
    # reemplaza username corriente por un correo
    class TipoUsuario(models.TextChoices):
        paciente = ("PCT", "Paciente")
        administrador = ("ADM", "Administrador")

    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    correo = models.CharField(max_length=50, unique=True, null=False)
    tipo_usuario = models.CharField(choices=TipoUsuario.choices, default=TipoUsuario.paciente)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "correo"
    EMAIL_FIELD = "correo"
    REQUIRED_FIELDS = []


    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - {self.tipo_usuario}"
    
class CentroMedico(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    direccion = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Especialista(models.Model):
    class Especialidad(models.TextChoices):
        CIRUGIA_GENERAL = "CG", "Cirugía General"
        CIRUGIA_CARDIOVASCULAR = "CCV", "Cirugía Cardiovascular"
        CIRUGIA_PEDIATRICA = "CPD", "Cirugía Pediátrica"
        CIRUGIA_PLASTICA_Y_REPARADORA = "CPR", "Cirugía Plástica y Reparadora"
        DERMATOLOGIA = "DMT", "Dermatología"
        GINECOLOGIA_Y_OBSTETRICIA = "GO", "Ginecología y Obstetricia"
        PSIQUIATRIA = "PSQ", "Psiquiatría"
        TRAUMATOLOGIA = "TMT", "Traumatología"
        ANESTESIOLOGIA = "ANS", "Anestesiología"
         
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    especialidad = models.CharField(choices=Especialidad.choices)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    
class Agenda(models.Model):
    fecha_disponible = models.DateField()
    hora_disponible = models.TimeField()
    especialista_id = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    centro_medico_id = models.ForeignKey(CentroMedico, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Consulta con {self.especialista_id}, a las {self.hora_disponible}"

class Cita(models.Model):
    agenda_id = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mensaje = models.TextField()


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    correo = models.EmailField()
    nombre = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return f"Formulario de contacto: {self.correo}"