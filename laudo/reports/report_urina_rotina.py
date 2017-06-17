"""
    Report: Urina Rotina
    Criado por: Leonardo Nascimento Cintra
    Data: 10/06/2017
"""
from datetime import datetime
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak
from reportlab.lib.pagesizes import A4

from paciente.models import Paciente
from medico.models import Medico
from exame.models import Exame
from laudo.models import Laudo, ExameLaudo, AssinadorEletronico
from laudo.reports import base_report

def gerar_laudo_urina_rotina(resquest, laudo_id):
    laudo = Laudo.objects.get(pk=laudo_id)
    p = Paciente.objects.get(pk=laudo.paciente.id)
    medico = Medico.objects.get(pk=laudo.medico.id)

    nome_sem_acento = base_report.remover_acentos(p.nome).replace(" ", "_")
    filename = "laudo_{}".format(nome_sem_acento)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(filename)

    c = canvas.Canvas(response, pagesize=A4)

    base_report.write_title(c)
    base_report.write_footer(c)

    c.setTitle("Laudo de {}".format(p.nome))
    c.showPage()
    c.save()
    return response