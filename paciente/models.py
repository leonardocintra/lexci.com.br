from datetime import date, datetime
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from convenio.models import Convenio
from .constants import RACA, SEXO


class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    cartao_sus = models.CharField('SUS', max_length=15, blank=True, null=True)
    nome_mae = models.CharField('Nome da mãe', max_length=150, blank=True, null=True)
    apelido = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField('CPF', unique=True, max_length=11)
    nacionalidade = models.CharField(max_length=100, default='brasileira', blank=True, null=True)
    data_nascimento = models.DateField()
    raca = models.CharField('Raça', choices=RACA, default='BRA', max_length=3)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    profissao = models.CharField(max_length=200, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, null=True)

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
            birthday = data_nascimento.replace(year=today.year, month=data_nascimento.month + 1, day=1)
        if birthday > today:
            return today.year - data_nascimento.year - 1
        else:
            return today.year - data_nascimento.year


class PacienteEndereco(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=100)
    numero_casa = models.CharField('Nº casa',max_length=10, blank=True, default='')
    complemento = models.CharField(max_length=50, blank=True, default='')
    bairro = models.CharField(max_length=50, blank=True, default='')
    uf = models.CharField('UF', max_length=2)
    codigo_municipio = models.IntegerField('Codigo Municipio', blank=True, null=True)
    municipio = models.CharField(max_length=100)
    cep = models.CharField('CEP', max_length=8, blank=True, default='')
    fone_ddd = models.CharField('DDD:', max_length=2, blank=True, default='')
    fone_numero = models.CharField('Telefone:', max_length=11) # Michele disse que esse campo é Obrigatorio
    email = models.EmailField(blank=True, default='')
    ponto_de_referencia = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.paciente.nome + ' | ' + self.municipio + ' - ' + self.uf

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'