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
from laudo.views import laudo as laudo_view
from laudo.reports import base_report


def write_laudo(canvas, laudo):
    c = canvas