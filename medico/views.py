from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from .models import Medico


class ListMedico(ListView):
    model = Medico
    template_name = 'medico/medico_list.html'
    context_object_name = 'medico_list'


medico_list = ListMedico.as_view()
