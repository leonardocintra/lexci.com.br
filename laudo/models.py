""" 
    Laudo Model
    Criado por: Leonardo Nascimento Cintra
    Data: janeiro/2017
"""
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from paciente.models import Paciente
from medico.models import Medico
from exame.models import Exame, ItemExame


class AssinadorEletronico(models.Model):
    """ 
        AssinadorEletronico - São os usuarios que tem permissao para assinar eletronicamente
        Descrição dos campos:
            - nome_exibir: O nome do assinador, pois no usuario nao fica o nome com os tratamentos. Ex: Dr. Marcio ...
            - profissao: É a descrição da profissao do assinador, ex: Biomedico Citologico
            - registro_federal: é o CRM ou registro junto ao orgão federal, ex: CRBM 8803/SBCC 768
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome_exibir = models.CharField('Nome', max_length=200, blank=True)
    profissao = models.CharField('Profissão', max_length=200, blank=True)
    registro_federal = models.CharField('Descrição dos regitro', max_length=200, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    foto_assinatura = models.ImageField('Assinatura', null=True, upload_to='laudo/media/')


    class Meta:
        """ Assinador Eletronico Meta """
        verbose_name = 'Assinador'
        verbose_name_plural = 'Assinadores'
    
    def __str__(self):
        return '{} - {}'.format(self.user.username, self.user.name)


class Laudo(models.Model):
    """ Laudo - É o laudo em si. Inclui o paciente, medico.
        Descrição dos campos:
            - paciente: é o paciente (id)
            - medico: médico que atendeu (id)
            - ultima_menstruacao: gravará a data da ultima menstruação que precisa constar nos laudos
            - paciente_pode_ver: o laudo é publico ou nao? O Paciente pode consultar o laudo dele on line
            - ativo: nao sera de costume deletar os laudos. Apenas inativa - los
            - assinado: se o laudo ja foi assinado ou nao
            - assinado_por: é o ID do usuario que assinou
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_coleta = models.DateTimeField('Data da coleta')
    ultima_menstruacao = models.DateTimeField('Data ultima menstruação')
    paciente_pode_ver = models.BooleanField(default=False)
    assinado = models.BooleanField(default=False)
    assinado_por = models.ForeignKey(AssinadorEletronico, on_delete=models.CASCADE, 
        related_name='assinador', blank=True, null=True
    )
    data_assinatura = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Laudo'
        verbose_name_plural = 'Laudos'
        ordering = ['-data_cadastro', ]
    
    def __str__ (self):
        return self.paciente.nome


class ExameLaudo(models.Model):
    """ ExameLaudo - Aqui é onde amarra os laudos com o exame """
    laudo = models.ForeignKey(Laudo, on_delete=models.CASCADE, related_name='laudo')
    item_exame = models.ForeignKey(ItemExame, on_delete=models.CASCADE, 
        related_name='item_exame'
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Exame Laudo'
    
    def __str__ (self):
        return self.item_exame.descricao_item