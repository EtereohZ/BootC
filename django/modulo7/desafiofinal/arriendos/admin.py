from django.contrib import admin
from .models import CustomUser, Inmuebles, Regiones, Comunas
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "modificado", "last_login")
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('custom_field',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Inmuebles)


