from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from fm.views import AjaxCreateView

from .models import Medico


class MedicoList(LoginRequiredMixin, ListView):
    model = Medico
    template_name = 'medico/medico_list.html'
    context_object_name = 'medico_list'


class CreateMedico(AjaxCreateView):
    model = Medico
    fields = ['nome', 'crm', 'telefone', ]

    def get_success_url(self):
        return reverse_lazy('medico:medico_list')


class MedicoDetail(LoginRequiredMixin, DetailView):
    model = Medico

    def get_context_data(self, **kwargs):
        context = super(MedicoDetail, self).get_context_data(**kwargs)
        return context

    
class MedicoUpdate(LoginRequiredMixin, UpdateView):
    model = Medico
    fields = ['nome', 'crm', 'telefone']

    def get_success_url(self):
        return reverse_lazy('medico:medico_list')

    def get_context_data(self, **kwargs):
        context = super(MedicoUpdate, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['nome'] = get_object_or_404(Medico, pk=self.kwargs['pk'])
        return context


class MedicoDelete(LoginRequiredMixin, DeleteView):
    model = Medico

    def get_success_url(self):
        return reverse_lazy('medico:medico_list')




medico_list = MedicoList.as_view()
medico_create = CreateMedico.as_view()
medico_detail = MedicoDetail.as_view()
medico_update = MedicoUpdate.as_view()
medico_delete = MedicoDelete.as_view()