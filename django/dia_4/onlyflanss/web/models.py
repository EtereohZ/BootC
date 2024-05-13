from django.db import models
import uuid

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    nombre = models.CharField(max_length=64)
    descripcion = models.TextField()
    img_url = models.FileField()
    slug = models.SlugField(default="", null=True)
    is_private = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.nombre}"
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return f"Formulario de contacto: {self.customer_email}"