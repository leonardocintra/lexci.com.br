from django.db import models

class Convenio(models.Model):
    descricao = models.CharField(max_lengt=100)
    slug = models.SlugField('Identificador', max_length=100)

    class Meta:
        verbose_name = 'Convenio'
        verbose_name = 'Convenios'
        ordering = ['descricao']
    
    def __str__ (self):
        return self.descricao
