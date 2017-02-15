from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView
from django.views.generic.detail import DetailView
from fm.views import AjaxCreateView, AjaxUpdateView

from .models import Medico


class ListMedicoView(ListView):
    model = Medico
    template_name = 'medico/medico_list.html'
    context_object_name = 'medico_list'


class CreateMedicoView(AjaxCreateView):
    model = Medico
    fields = ['nome', 'crm', 'telefone', ]

    def get_success_url(self):
        return reverse_lazy('medico:medico_list')


class DetailMedicoView(DetailView):
    model = Medico

    def get_context_data(self, **kwargs):
        context = super(DetailMedicoView, self).get_context_data(**kwargs)
        return context

    
class UpdateMedicoView(UpdateView):
    model = Medico
    fields = ['nome', 'crm', 'telefone']

    def get_success_url(self):
        return reverse_lazy('medico:medico_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateMedicoView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['nome'] = get_object_or_404(Medico, pk=self.kwargs['pk'])
        return context



medico_list = ListMedicoView.as_view()
medico_create = CreateMedicoView.as_view()
medico_detail = DetailMedicoView.as_view()
medico_update = UpdateMedicoView.as_view()