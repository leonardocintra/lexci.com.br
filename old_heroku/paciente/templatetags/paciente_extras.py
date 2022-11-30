from django.template import Library
from laudo.views import laudo
from paciente.models import Paciente

register = Library()

@register.assignment_tag
def get_idade_paciente(data_nascimento):
    return Paciente.calcula_idade(data_nascimento)

@register.simple_tag
def get_tipo_exame(laudo_id):
    tipo_laudo = laudo.get_tipo_exame_laudo(laudo_id)
    return laudo.get_descricao_tipo_exame_laudo(tipo_laudo)