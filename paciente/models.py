from datetime import date, datetime
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from .constants import RACA


class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    cartao_sus = models.CharField('SUS', unique=True, max_length=15)
    nome_mae = models.CharField('Nome da mãe', max_length=150)
    apelido = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField('CPF', unique=True, max_length=11)
    nacionalidade = models.CharField(max_length=100, default='brasileira')
    data_nascimento = models.DateField()
    raca = models.CharField('Raça', choices=RACA, default='BRA', max_length=3)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

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


class PacienteEndereco(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=100)
    numero_casa = models.CharField('Nº casa',max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    uf = models.CharField('UF', max_length=2)
    codigo_municipio = models.IntegerField('Codigo Municipio')
    municipio = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField('CEP', max_length=8)
    fone_ddd = models.CharField('DDD:', max_length=2, blank=True, null=True)
    fone_numero = models.CharField('Telefone:', max_length=11, blank=True, null=True)
    ponto_de_referencia = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.paciente.nome + ' - ' + self.municipio

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


# Signails
@receiver(signals.post_save, sender=Paciente)
def paciente_post_save(sender, instance, created, **kwargs):
    # salvar o endereco tambem
    if created:
        print(instance.id)
        print(instance.nome)