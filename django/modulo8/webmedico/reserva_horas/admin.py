from django.contrib import admin
from .models import CustomUser, CentroMedico, Especialista, Agenda, Cita, ContactForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    # Aquí logramos que los objectos mencionados abajo solo se puedan leer
    readonly_fields = ("creado", "modificado", "last_login")
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('custom_field',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CentroMedico)
admin.site.register(Especialista)
admin.site.register(Agenda)
admin.site.register(Cita)
admin.site.register(ContactForm)