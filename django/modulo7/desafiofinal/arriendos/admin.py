from django.contrib import admin
from .models import CustomUser, Inmuebles, Regiones, Comunas

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "modificado")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Inmuebles)


