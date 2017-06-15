# -*- coding: utf-8 -*-
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


def gerar_laudo(request, laudo_id):
    laudo = Laudo.objects.get(pk=laudo_id)
    p = Paciente.objects.get(pk=laudo.paciente.id)
    medico = Medico.objects.get(pk=laudo.medico.id)

    nome_sem_acento = base_report.remover_acentos(p.nome)
    filename = "laudo_{}".format(nome_sem_acento)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(filename)

    c = canvas.Canvas(response, pagesize=A4)

    base_report.write_title(c)

    write_paciente(c, p, medico)

    base_report.write_horizontal_line(c, 670)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(55, 650, 'EXAME CITOPATOLÓGICO CERVICAL UTERINO, (Bethesda 2001)')
    base_report.write_horizontal_line(c, 640)

    c.setFont('Helvetica-Bold', 12)
    c.drawString(40, 620, 'Data da coleta: ')
    c.setFont('Helvetica', 12)
    c.drawString(130, 620, '{}'.format(str(laudo.data_coleta.strftime('%d/%m/%Y'))))
    c.setFont('Helvetica-Bold', 12)
    c.drawString(40, 600, 'Data da ultima menstruação:')
    c.setFont('Helvetica', 12)
    c.drawString(209, 600, '{}'.format(str(laudo.ultima_menstruacao.strftime('%d/%m/%Y'))))

    write_exames(c, laudo)

    write_assinatura(c, laudo)
    base_report.write_footer(c)

    c.setTitle("Laudo de {}".format(p.nome))
    c.showPage()
    c.save()

    return response

def write_exames(canvas, laudo):
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
                write_footer(c)
                write_assinatura(c, laudo)
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


def write_paciente(canvas, paciente, medico):
    c = canvas
    p = paciente

    tamanho_letra = 14

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(45, 720, 'Nome: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(95, 720, p.nome)

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(450, 720, 'Idade: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(495, 720, '{} anos'.format(Paciente.calcula_idade(p.data_nascimento)))

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(45, 700, 'Médico: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(105, 700, medico.nome)

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(450, 700, 'Sexo: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(490, 700, p.get_sexo_display())

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(45, 680, 'Convênio: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    varConvenio = ""
    if p.convenio:
        varConvenio = p.convenio.descricao
    else:
        varConvenio = ""
    c.drawString(115, 680, varConvenio)

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(450, 680, 'Código: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(505, 680, '#{}'.format(p.id))
    return c


def write_assinatura(canvas, laudo):
    """ 
        Pega a assinatura do Marcio ou Michelle por exempo 
        Precisa reconfigurar isso para funcionar corretamente
    """
    c = canvas
    c.setFont('Helvetica-Oblique', 10)

    if laudo.assinado:
        assinador = AssinadorEletronico.objects.get(pk=laudo.assinado_por.id)        
        if assinador.foto_assinatura:
            c.drawImage('{}'.format(assinador.foto_assinatura.url), 440, 95, 120, 40)
        c.setFont('Helvetica-Bold', 10)
        c.drawString(440, 90, assinador.nome_exibir)
        c.setFont('Helvetica-Oblique', 10)
        c.drawString(455, 76, assinador.profissao)
        c.drawString(453, 61, assinador.registro_federal)
    else:
        c.drawString(450, 90, '-- ATENÇÂO! --')
        c.setFont('Helvetica-Bold', 10)
        c.drawString(430, 76, 'LAUDO NÃO ASSINADO')
        c.setFont('Helvetica-Oblique', 10)
        c.drawString(443, 61, 'Documento Inválido!')
    return c
