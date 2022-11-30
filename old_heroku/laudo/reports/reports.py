# -*- coding: utf-8 -*-
from datetime import datetime
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak
from reportlab.lib.pagesizes import A4

from paciente.models import Paciente
from medico.models import Medico
from exame.models import Exame
from laudo.models import Laudo, ExameLaudo
from laudo.reports import base_report, citopatologico_cervical_uterino, urina_rotina
from laudo.views import laudo as laudo_view


def gerar_laudo(request, laudo_id):
    laudo = Laudo.objects.get(pk=laudo_id)
    p = Paciente.objects.get(pk=laudo.paciente.id)
    medico = Medico.objects.get(pk=laudo.medico.id)
    

    # Monta dados do file (PDF)
    nome_sem_acento = base_report.remover_acentos(p.nome).replace(" ", "_")
    filename = "laudo_{}".format(nome_sem_acento)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(filename)
    c = canvas.Canvas(response, pagesize=A4)

    # Escreve o cabeçalho do PDF
    base_report.write_title(c)

    # Escreve dados do paciente
    base_report.write_paciente(c, p, medico)
    base_report.write_horizontal_line(c, 670)

    id_tipo_laudo = laudo_view.get_tipo_exame_laudo(laudo_id)
    
    # Escreve o tipo de exame
    c.setFont('Helvetica-Bold', 16)
    c.drawString(55, 650, laudo_view.get_descricao_tipo_exame_laudo(id_tipo_laudo))
    base_report.write_horizontal_line(c, 640)

    # Escreve o exame conforme id
    if id_tipo_laudo == 1: 
        # 1 = Exame Citopatologico Cervical Uterino
        citopatologico_cervical_uterino.write_laudo(c, laudo)
    elif id_tipo_laudo == 2: 
        # 2 = Urina Rotina - Método Convencional
        urina_rotina.write_laudo(c, laudo)
    elif id_tipo_laudo == 3:
        # 3 = Colesterol e Glicose
        pass
    else:
        pass

    base_report.write_assinatura(c, laudo)
    base_report.write_footer(c)

    c.setTitle("Laudo de {}".format(p.nome))
    c.showPage()
    c.save()
    return response