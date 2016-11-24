from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Paciente


class ListPaciente(ListView):
    model = Paciente
    template_name = 'paciente/paciente_list.html'
    context_object_name = 'paciente_list'


class CreatePaciente(CreateView):
    model = Paciente
    fields = ['nome', 'cartao_sus', 'nome_mae', 'apelido', 'cpf', 'nacionalidade', 'data_nascimento', 'raca', 'ativo']
    success_url = reverse_lazy('paciente:paciente_list')


paciente_list = ListPaciente.as_view()
paciente_create = CreatePaciente.as_view()
