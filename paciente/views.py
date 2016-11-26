from django.shortcuts import render
from django.db import transaction
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Paciente
from .forms import PacienteForm, EnderecoPacienteFormSet


class ListPaciente(ListView):
    model = Paciente
    template_name = 'paciente/paciente_list.html'
    context_object_name = 'paciente_list'


class CreatePaciente(CreateView):
    model = Paciente
    template_name = 'paciente_endereco_new.html'
    form_class = PacienteForm
    success_url = reverse_lazy('paciente:paciente_list')

    def get(self, request, *args, **kwargs):
        pass



paciente_list = ListPaciente.as_view()
paciente_create = CreatePaciente.as_view()
