"""
    Report: Exame Citopatologico Cervical Uterino
    Criado por: Leonardo Nascimento Cintra
    Data: 17/06/2017
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
from laudo.views import laudo as laudo_view
from laudo.reports import base_report

def write_laudo(canvas, laudo):
    c = canvas

    c.setFont('Helvetica-Bold', 12)
    c.drawString(40, 620, 'Data da coleta: ')
    c.setFont('Helvetica', 12)
    if laudo.data_coleta:
        c.drawString(130, 620, '{}'.format(str(laudo.data_coleta.strftime('%d/%m/%Y'))))
    c.setFont('Helvetica-Bold', 12)
    c.drawString(40, 600, 'Data da ultima menstruação:')
    c.setFont('Helvetica', 12)
    c.drawString(209, 600, '{}'.format(str(laudo.ultima_menstruacao.strftime('%d/%m/%Y'))))

    __write_exames(c, laudo)

def __write_exames(canvas, laudo):
    c = canvas
    exame_laudos = ExameLaudo.objects.filter(laudo=laudo)
    contador = exame_laudos.count()
    exames = Exame.objects.all()

    espacamento = 590
    exame_atual = ""
    for exame in exames:
        for item in exame_laudos:
            if espacamento < 90:
                espacamento = 820
                base_report.write_footer(c)
                base_report.write_assinatura(c, laudo)
                c.showPage()
            if item.item_exame.exame.id == exame.id:
                if exame_atual != item.item_exame.exame.descricao:
                    espacamento -= 24
                    c.setFont('Helvetica-Bold', 12)
                    c.drawString(40, espacamento, item.item_exame.exame.descricao)
                    exame_atual = item.item_exame.exame.descricao
                espacamento -= 14
                c.setFont('Helvetica', 9)
                c.drawString(40, espacamento, "  - {}".format(item.item_exame.descricao_item))                
    return c