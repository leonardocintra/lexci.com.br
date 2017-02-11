from django.db import models
from paciente.models import Paciente
from medico.models import Medico
from core.models import Convenio


class Exame(models.Model):
    """ Exames - tabela que salva os tipos de exames que são inseridos no laudo. 
        Campos:
            - descricao: descreve o nome do exame (titulo)
    """
    descricao = models.CharField('Descrição', max_length=200)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Exame do Laudo'
        verbose_name_plural = 'Exames do Laudo'
        ordering = ['descricao']
    
    def __str__ (self):
        return self.descricao

    class Meta:
        pass


class ItemExame(models.Model):
    """ ItemExame - Apos cadastrar o exame, cada exam tem os items do tipo de exame realizado 

        Ex: 
        EXAME: TIPO DA AMOSTRA:
        Itens Exame:
            - ESFREGAÇO CONVENCIONAL
            - CITOLOGIA LÍQUIDA

        EXAME: ADEQUAÇÃO DA AMOSTRA:
        Itens Exame:
            - SATISFATÓRIA
            - LIMITADA
            - INSATISFATÓRIA
    """
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE, related_name='exame')
    descricao_item = models.CharField('Descrição', max_length=300)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Item exame'
        verbose_name_plural = 'Itens dos Exame'
        ordering = ['descricao_item']

    def __str__ (self):
        return self.descricao_item



class Laudo(models.Model):
    """ Laudo - É o laudo em si. Inclui o paciente, medico, convenio o os items que vai nele 
        Descrição dos campos:
            - paciente: é o paciente (id)
            - medico: médico que atendeu (id)
            - convenio: tipo de convenio (id)
            - exames: todos os exames realizados 
            - paciente_pode_ver: o laudo é publico ou nao? O Paciente pode consultar o laudo dele on line
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    exames = models.ManyToManyField(ItemExame)
    paciente_pode_ver = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Laudo'
        verbose_name_plural = 'Laudos'
    
    def __str__ (self):
        return self.paciente.nome