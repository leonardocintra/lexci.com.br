from datetime import date, datetime
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

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['nome']
    
    def __str__ (self):
        return self.nome
    
    def calcula_idade(data_nascimento):
        today = date.today()
        try: 
            birthday = data_nascimento.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = data_nascimento.replace(year=today.year, month=data_nascimento.month+1, day=1)
        if birthday > today:
            return today.year - data_nascimento.year - 1
        else:
            return today.year - data_nascimento.year