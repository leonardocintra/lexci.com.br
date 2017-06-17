from reportlab.pdfgen import canvas
from unicodedata import normalize


def write_title(canvas):
    organizador = 20

    c = canvas
    c.setFont('Helvetica-BoldOblique', 10)
    c.drawImage("core/static/images/logolexci.png", 90, 760, 120, 40)
    c.drawString(340 - organizador, 820, 'LABORATÓRIO DE EXAMES CITOLÓGICOS')
    c.drawString(285 - organizador, 805, 'Rua Marechal Floriano Peixoto 295 – Bairro Centro – Ibiraci – MG')
    c.drawString(360 - organizador, 790, '(35) 9.9991-8888 / (16) 99408-0682')
    c.setFont('Helvetica-Oblique', 8)
    c.drawString(340 - organizador, 775, 'e-mail: atendimento@lexci.com.br / marcio@lexci.com.br')
    c.setFont('Helvetica-BoldOblique', 10)
    c.drawString(345 - organizador, 760, 'Responsável: Dr Márcio Gimenes França')
    c.drawString(330 - organizador, 745, 'CRBM 8803 Inscrição: 16/3453 CNES: 9088148')
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


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')     