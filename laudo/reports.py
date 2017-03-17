# -*- coding: utf-8 -*-

from datetime import datetime
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak
from reportlab.lib.pagesizes import A4

from paciente.models import Paciente
from medico.models import Medico
from laudo.models import Laudo, ExameLaudo, Exame


def gerar_laudo(request, laudo_id, paciente_id):

    p = Paciente.objects.get(pk=paciente_id)
    laudo = Laudo.objects.get(pk=laudo_id)
    medico = Medico.objects.get(pk=laudo.medico.id)

    filename = "laudo_{}".format(p.nome)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(filename)

    c = canvas.Canvas(response, pagesize=A4)

    write_title(c)

    write_paciente(c, p, medico)

    write_horizontal_line(c, 670)
    c.setFont('Helvetica-Bold', 16)
    c.drawString(55, 650, 'EXAME CITOPATOLÓGICO CERVICAL UTERINO, (Bethesda 2001)')
    write_horizontal_line(c, 640)

    c.setFont('Helvetica-Bold', 12)
    c.drawString(40, 620, 'Data da coleta: ')
    c.setFont('Helvetica', 12)
    c.drawString(130, 620, '{}'.format(str(datetime.now().strftime('%d/%m/%Y - %H:%M h'))))
    c.setFont('Helvetica-Bold', 12)
    c.drawString(40, 600, 'Data da ultima menstruação: ')

    write_exames(c, laudo)

    write_assinatura_marcio(c)
    write_footer(c)

    c.setTitle("Laudo de {}".format(p.nome))
    c.showPage()
    c.save()

    return response

def write_exames(canvas, laudo):
    c = canvas
    item_exames = ExameLaudo.objects.filter(laudo=laudo)
    contador = item_exames.count()
    exames = Exame.objects.all()

    espacamento = 590
    exame_atual = ""
    for exame in exames:
        for item in item_exames:
            if espacamento < 90:
                espacamento = 820
                write_footer(c)
                write_assinatura_marcio(c)
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

    #variavel.decode('utf-8')

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
    c.drawString(495, 700, 'FEMININO')

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

def write_assinatura_marcio(canvas):
    c = canvas
    c.setFont('Helvetica-Oblique', 10)
    c.drawString(440, 90, 'Dr. Márcio Gimenes França')
    c.drawString(455, 76, 'Biomédico Citologista')
    c.drawString(453, 61, 'CRBM 8803/SBCC 768')
    return c

def write_title(canvas):
    c = canvas
    c.setFont('Helvetica-BoldOblique', 10)
    c.drawImage("core/static/images/logolexci.png", 90, 760, 120, 40)
    c.drawString(350, 820, 'LABORATÓRIO DE EXAMES CITOLÓGICOS')
    c.drawString(320, 805, 'Rua Coronel Timóteo 91 - Bairro Centro - Ibiraci - MG')
    c.drawString(330, 790, '(35) 3544-1044 / (35) 9.9991-8888 / (16) 99408-0682')
    c.setFont('Helvetica-Oblique', 8)
    c.drawString(360, 775, 'e-mail: atendimento@lexci.com.br / marcio@lexci.com.br')
    c.setFont('Helvetica-BoldOblique', 10)
    c.drawString(355, 760, 'Responsável: Dr Márcio Gimenes França')
    c.drawString(340, 745, 'CRBM 8803 Inscrição: 16/3453 CNES: 9088148')
    write_horizontal_line(c, 740)
    return c


def write_footer(canvas):
    c = canvas
    write_horizontal_line(c, 35)
    c.setFont('Helvetica-Oblique', 10)
    c.drawString(20, 25, 'Laudo segundo o Sistema Bethesda, (The 2001 Bethesda System Terminology, November 5, 2003 Bethesda Maryland USA).')
    c.drawString(20, 15, 'Membro da sociedade brasileira de citologia clínica')

    return c


def write_horizontal_line(canvas, vertical_point):
    """ Desenha a linha horizontal (traço)"""
    c = canvas
    c.setFontSize(9)
    c.line(20, vertical_point, 580, vertical_point)
    return c


