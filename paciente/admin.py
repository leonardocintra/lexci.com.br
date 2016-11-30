from django.contrib import admin
from .models import Paciente, PacienteEndereco


class PacienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'cartao_sus', 'nome_mae', 'apelido', 'cpf', 'nacionalidade', 'data_nascimento', 'raca', 'profissao', 'ativo')

class PacienteEnderecoAdmin(admin.ModelAdmin):
    fields = ('logradouro', 'municipio', 'uf')

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(PacienteEndereco, PacienteEnderecoAdmin)