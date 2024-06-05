from django.contrib import admin
from .models import CustomUser, Inmuebles

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "modificado")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Inmuebles)

