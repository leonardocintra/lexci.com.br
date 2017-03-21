"""
    Exame Model
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.db import models



class Exame(models.Model):
    """ Exames - tabela que salva os tipos de exames que são inseridos no laudo.
        Campos:
            - descricao: descreve o nome do exame (titulo)
    """
    descricao = models.CharField('Descrição', max_length=200, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Exame do Laudo'
        verbose_name_plural = 'Exames do Laudo'
        ordering = ['descricao']

    def __str__ (self):
        return self.descricao


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
