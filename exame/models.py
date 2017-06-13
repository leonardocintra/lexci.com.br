"""
    Exame Model
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.db import models



class Exame(models.Model):
    """ Exames - tabela que salva os tipos de exames que são inseridos no laudo.
        Campos:
            - nome: nome do exame
            - descricao: descreve o nome do tipo de exame
    """
    NOME_EXAME = (
        (1, 'EXAME CITOPATOLÓGICO CERVICAL UTERINO'),
        (2, 'Urina Rotina - Método Convencional'),
        (3, 'Glicose / Colesterol'),
    )
    nome = models.IntegerField(choices=NOME_EXAME, default=1)
    descricao = models.CharField('Descrição', max_length=200, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    ordem_exibicao = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Exame do Laudo'
        verbose_name_plural = 'Exames do Laudo'
        ordering = ['ordem_exibicao', ]

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
