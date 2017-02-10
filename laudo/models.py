from django.db import models

from paciente.models import Paciente
from medico.models import Medico
from core.models import Convenio


class Laudo(models.Model):
    """ Laudo - È o laudo em si. Inclui o paciente, medico, convenio o os items que vai nele """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    exames = models.ManyToManyField(ItemExame, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Laudo'
        verbose_name_plural = 'Laudos'
    
    def __str__ (self):
        return self.paciente.nome


class Exame(models.Model):
    """ Exames - tabela que salva os tipos de exames que são inseridos no laudo. """
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
    """ 
        ItemExame - Apos cadastrar o exame, cada exam tem os items do tipo de exame realizado 
        
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