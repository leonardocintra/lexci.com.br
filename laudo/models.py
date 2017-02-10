from django.db import models

from paciente.models import Paciente
from medico.models import Medico
from core.models import Convenio


class Laudo(models.Model):
    pass
    #paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='paciente')
    #medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='medico')
    #convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, related_name='convenio')