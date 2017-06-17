from reportlab.pdfgen import canvas
from unicodedata import normalize
from laudo.models import AssinadorEletronico

from paciente.models import Paciente


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


def get_tamanho_palavra(word):
    return len(word)