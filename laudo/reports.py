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


    c.showPage()
    c.save()

    return response


def write_title(obj_canvas):
    c = obj_canvas
    c.setFont('Helvetica-BoldOblique', 10)
    c.drawImage("core/static/images/logolexci.png", 90, 710, 120, 40)
    c.drawString(350, 770, 'LABORATÓRIO DE EXAMES CITOLÓGICOS')
    c.drawString(320, 755, 'Rua Coronel Timóteo 91 - Bairro Centro - Ibiraci - MG')
    c.drawString(330, 740, '(35) 3544-1044 / (35) 9.9991-8888 / (16) 99408-0682')
    c.setFont('Helvetica-Oblique', 8)
    c.drawString(360, 725, 'e-mail: atendimento@lexci.com.br / marcio@lexci.com.br')
    c.setFont('Helvetica-BoldOblique', 10)
    c.drawString(330, 710, 'Responsável: Dr Márcio Gimenes França')
    c.drawString(340, 695, 'CRBM 8803 Inscrição: 16/3453 CNES: 9088148')
    write_line_horizontal(c, 690)
    return c


def write_line_horizontal(obj_canvas, vertical_point):
    c = obj_canvas
    c.setFontSize(9)
    c.line(35, vertical_point, 580, vertical_point)
    return c


