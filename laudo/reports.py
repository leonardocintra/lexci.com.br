import datetime
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def gerar_laudo(request):

    filename = "LEXCI"
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(filename)

    c = canvas.Canvas(response, pagesize=letter)

    write_title(c)

    write_paciente(c)

    c.setFont('Helvetica-Bold', 16)
    c.drawString(55, 603, 'EXAME CITOPATOLÓGICO CERVICAL UTERINO, (Bethesda 2001)')
    write_horizontal_line(c, 595)

    write_footer(c)


    c.showPage()
    c.save()

    return response


def write_paciente(canvas):
    c = canvas

    tamanho_letra = 14

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(45, 670, 'Nome: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(95, 670, 'Leonardo Nascimento Cintra')

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(450, 670, 'Idade: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(495, 670, '27 anos')

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(45, 650, 'Médico: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(105, 650, 'Dr. Ronaldo Soares Lara')

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(450, 650, 'Sexo: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(495, 650, 'FEMININO')

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(45, 630, 'Convênio: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(115, 630, 'Unimed')

    c.setFont('Helvetica', tamanho_letra)
    c.drawString(450, 630, 'Código: ')
    c.setFont('Helvetica-Bold', tamanho_letra)
    c.drawString(505, 630, '#456866')

    write_horizontal_line(c, 620)
    return c


def write_title(canvas):
    c = canvas
    c.setFont('Helvetica-BoldOblique', 10)
    c.drawImage("core/static/images/logolexci.png", 90, 710, 120, 40)
    c.drawString(350, 770, 'LABORATÓRIO DE EXAMES CITOLÓGICOS')
    c.drawString(320, 755, 'Rua Coronel Timóteo 91 - Bairro Centro - Ibiraci - MG')
    c.drawString(330, 740, '(35) 3544-1044 / (35) 9.9991-8888 / (16) 99408-0682')
    c.setFont('Helvetica-Oblique', 8)
    c.drawString(360, 725, 'e-mail: atendimento@lexci.com.br / marcio@lexci.com.br')
    c.setFont('Helvetica-BoldOblique', 10)
    c.drawString(355, 710, 'Responsável: Dr Márcio Gimenes França')
    c.drawString(340, 695, 'CRBM 8803 Inscrição: 16/3453 CNES: 9088148')
    write_horizontal_line(c, 690)
    return c


def write_footer(canvas):
    c = canvas
    write_horizontal_line(c, 50)
    c.setFont('Helvetica-Oblique', 10)
    c.drawString(35, 40, 'Laudo segundo o Sistema Bethesda, (The 2001 Bethesda System Terminology, November 5, 2003 Bethesda Maryland USA).')
    c.drawString(35, 30, 'Membro da sociedade brasileira de citologia clínica')

    return c


def write_horizontal_line(canvas, vertical_point):
    """ Desenha a linha horizontal (traço)"""
    c = canvas
    c.setFontSize(9)
    c.line(35, vertical_point, 580, vertical_point)
    return c


