from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    # Manager con el que funciona el modelo "CustomUser"
    # Reemplaza username con correo
    # Se encarga de la creación de usuarios normales y superusers
    def create_user(self, correo:str, password:str, **extra_fields):
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, correo:str, password:str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(correo, password, **extra_fields)