from django.db import models


class Medico(models.Model):
    """ Model Medico - Medidos 'de fora' que realiza o exame """
    nome = models.CharField(max_length=200)
    crm = models.CharField('CRM', max_length=50, blank=True, null=True)
    telefone = models.CharField('Telefone:', max_length=20, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['nome']
    
    def __str__ (self):
        return self.nome