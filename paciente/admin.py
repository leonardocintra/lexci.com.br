from django.contrib import admin
from .models import Paciente


class PacienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'cartao_sus', 'nome_mae', 'apelido', 'cpf', 'nacionalidade', 'data_nascimento', 'raca', 'ativo')

admin.site.register(Paciente, PacienteAdmin)