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
from exame.models import Exame, SubExameItem
from laudo.models import Laudo, ExameLaudo, AssinadorEletronico, ExameUrinaRotina
from laudo.views import laudo as laudo_view
from laudo.reports import base_report


def write_laudo(canvas, laudo):
    c = canvas

    c.setFont('Helvetica-Bold', 12)
    c.drawString(40, 620, 'Data da coleta: ')
    c.setFont('Helvetica', 12)
    c.drawString(130, 620, '{}'.format(str(laudo.data_coleta.strftime('%d/%m/%Y'))))

    __write_exames(c, laudo)



def __write_exames(canvas, laudo):
    c = canvas
    exame_laudos = ExameLaudo.objects.filter(laudo=laudo)
    exames = Exame.objects.filter(nome=2)
    exames_urina_rotina = ExameUrinaRotina.objects.get(laudo=laudo)
    # Dados exame Carcterísticas Fisicas
    c.setFont('Helvetica-Bold', 12)
    c.drawString(40, 590, 'Características Físicas')
    
    c.setFont('Helvetica-Bold', 11)
    c.drawString(50, 570, 'Volume:')
    c.setFont('Helvetica', 11)
    c.drawString(180, 570, str(exames_urina_rotina.volume))

    espacamento = 570
    for exame in exames:
        for item in exame_laudos:
            if item.item_exame.exame.id == exame.id:
                espacamento -= 15
                c.setFont('Helvetica-Bold', 11)
                nome_exame = '{}{}'.format(item.item_exame.exame.descricao, ':')
                c.drawString(50, espacamento, nome_exame)
                c.setFont('Helvetica', 11)
                c.drawString(180, espacamento, item.item_exame.descricao_item)
                exame_atual = item.item_exame.exame.descricao
    

    espacamento -= 15
    c.setFont('Helvetica-Bold', 11)
    c.drawString(50, espacamento, 'PH:')
    c.setFont('Helvetica', 11)
    c.drawString(180, espacamento, str(exames_urina_rotina.ph_urina))
    return c

