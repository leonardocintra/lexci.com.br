from django.contrib import admin
from .models import Paciente


class PacienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'cartao_sus', )

admin.site.register(Paciente, PacienteAdmin)