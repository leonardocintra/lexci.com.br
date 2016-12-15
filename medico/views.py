from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView

from .models import Medico


class ListMedicoView(ListView):
    model = Medico
    template_name = 'medico/medico_list.html'
    context_object_name = 'medico_list'


class CreateMedicoView(CreateView):
    model = Medico
    fields = ['nome', 'crm', 'telefone', ]


    def get_success_url(self):
        return reverse_lazy('medico:medico_list')


class DetailMedicoView(DetailView):
    model = Medico

    def get_context_data(self, **kwargs):
        context = super(DetailMedicoView, self).get_context_data(**kwargs)
        return context



medico_list = ListMedicoView.as_view()
medico_create = CreateMedicoView.as_view()
medico_detail = DetailMedicoView.as_view()
