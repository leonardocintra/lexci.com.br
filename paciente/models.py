from django.db import models
from .constants import RACA

class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    cartao_sus = models.CharField('SUS', unique=True, max_length=15)
    name_mae = models.CharField('Nome da mãe', max_length=200)
    apelido = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField('CPF', unique=True, max_length=11)
    nacionalidade = models.CharField(max_length=100, default='brasileira')
    data_nascimento = models.DateField()
    raca = models.CharField('Raça', choices=RACA, default='BRA')