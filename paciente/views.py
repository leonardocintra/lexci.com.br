from django.shortcuts import render
from django.views.generic import ListView
from .models import Paciente


class ListPaciente(ListView):
    model = Paciente
    template_name = 'paciente/paciente_list.html'
    context_object_name = 'paciente_list'


paciente_list = ListPaciente.as_view()
