from django.template import Library
from paciente.models import Paciente

register = Library()

@register.assignment_tag
def get_idade_paciente(data_nascimento):
    return Paciente.calcula_idade(data_nascimento)