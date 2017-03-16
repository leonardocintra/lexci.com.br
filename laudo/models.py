from django.db import models
from paciente.models import Paciente
from medico.models import Medico


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
    """ Laudo - É o laudo em si. Inclui o paciente, medico.
        Descrição dos campos:
            - paciente: é o paciente (id)
            - medico: médico que atendeu (id)
            - paciente_pode_ver: o laudo é publico ou nao? O Paciente pode consultar o laudo dele on line
            - ativo: nao sera de costume deletar os laudos. Apenas inativa - los
    """
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente_pode_ver = models.BooleanField(default=False)
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
    item_exame = models.ForeignKey(ItemExame, on_delete=models.CASCADE, related_name='item_exame')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Exame Laudo'
    
    def __str__ (self):
        return self.item_exame.descricao_item