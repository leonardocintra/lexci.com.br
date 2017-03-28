# -*- coding: utf-8 -*-
"""
    View Laudo
    Criado por Leonardo Cintra
    Data: 02/2017
"""
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, FormView, UpdateView, DetailView, CreateView
from paciente.models import Paciente
from exame.models import Exame, ItemExame
from .models import Laudo, ExameLaudo, AssinadorEletronico
from .forms import LaudoForm, AssinarLaudoEletronicoForm


class LudoDetail(DetailView):
    model = Laudo
    template_name = 'laudo/laudo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LudoDetail, self).get_context_data(**kwargs)
        context['paciente'] = get_object_or_404(Paciente, pk=self.kwargs['paciente_id'])
        context['exames'] = Exame.objects.all()
        context['item_exame'] = ItemExame.objects.all()
        context['exame_laudos'] = ExameLaudo.objects.filter(laudo_id=self.kwargs['pk'])
        return context


class LaudoCreate(FormView):
    """ Gerador do Laudo """

    template_name = 'laudo/laudo_form.html'
    model = Laudo
    form_class = LaudoForm

    def get_initial(self):
        return {
            "paciente" : self.kwargs['pk']
        }

    def form_valid(self, form):
        self.object = form.save()
        item_exames_ids = self.request.POST.getlist("item_exames")
        form.create_laudo_exames(self.object, item_exames_ids)

        return HttpResponseRedirect(self.get_success_url())


    def get_context_data(self, **kwargs):
        context = super(LaudoCreate, self).get_context_data(**kwargs)
        context['paciente'] = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        context['exames'] = Exame.objects.all()
        context['item_exame'] = ItemExame.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('paciente:paciente_detail', kwargs={'pk': self.kwargs['pk']})


class LaudoUpdate(UpdateView):
    model = Laudo
    fields = ['paciente_pode_ver']
    template_name = 'laudo/laudo_update.html'

    def get_success_url(self):
        return reverse_lazy('laudo:laudo_detalhe', kwargs={
            'pk': self.kwargs['pk'], 'paciente_id': self.kwargs['paciente_id']})

    
class LaudoAssinatura(FormView):
    template_name = 'laudo/assinatura_eletronica.html'
    model = Laudo
    form_class = AssinarLaudoEletronicoForm

    def get_initial(self):
        return {
            "assinado_por": self.request.user.id
        }

    def form_valid(self, form):
        laudo = get_object_or_404(Laudo, pk=self.kwargs['pk'])
        assinador = get_object_or_404(AssinadorEletronico, user=self.request.user.id)
        laudo.assinado_por = assinador
        laudo.assinado = True
        laudo.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_context_data(self, **kwargs):
        context = super(LaudoAssinatura, self).get_context_data(**kwargs)
        context['paciente'] = get_object_or_404(Paciente, pk=self.kwargs['paciente_id'])
        context['laudo'] = get_object_or_404(Laudo, pk=self.kwargs['pk'])
        return context
    
    def get_success_url(self):
        return reverse_lazy('paciente:paciente_detail', kwargs={'pk': self.kwargs['paciente_id']})



create_laudo = LaudoCreate.as_view() 
laudo_detalhe = LudoDetail.as_view() 
laudo_update = LaudoUpdate.as_view()
laudo_assinatura = LaudoAssinatura.as_view()