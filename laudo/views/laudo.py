# -*- coding: utf-8 -*-
"""
    View Laudo
    Criado por Leonardo Cintra
    Data: fevereiro/2017
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, FormView, UpdateView, DetailView, CreateView
from django.utils import timezone
from paciente.models import Paciente
from exame.models import Exame, ItemExame, NOME_EXAME
from laudo.models import Laudo, ExameLaudo, AssinadorEletronico, ExameUrinaRotina
from laudo.forms import LaudoForm, AssinarLaudoEletronicoForm, ExameLaudoForm


"""
                    ******  ATENÇÃO!! *****
    ==========================================================
    RENOMEAR ESSA VIEW PARA citopatologico_cervical_uterino.py
    ==========================================================
"""


class LaudoDetail(LoginRequiredMixin, DetailView):
    model = Laudo
    template_name = 'laudo/laudo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LaudoDetail, self).get_context_data(**kwargs)
        exames = []
        exame_laudo = ExameLaudo.objects.filter(laudo_id=self.kwargs['pk'])
        for item in exame_laudo:
            exames.append(item.item_exame.exame.id)
        context['exames'] = Exame.objects.filter(pk__in=exames)
        context['exame_laudo'] = exame_laudo
        tipo_exame = get_tipo_exame_laudo(self.kwargs['pk'])
        context['descricao_tipo_exame'] = get_descricao_tipo_exame_laudo(tipo_exame)
        context['id_tipo_exame'] = get_id_tipo_exame_laudo(tipo_exame)
        context['exames_urina_rotina'] = ExameUrinaRotina.objects.filter(laudo_id=self.kwargs['pk'])
        return context



class LaudoCreate(LoginRequiredMixin, FormView):
    """ Gerador do Laudo """
    model = Laudo
    template_name = 'laudo/laudo_form.html'
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
        context['exames'] = Exame.objects.filter(nome=1)
        context['item_exame'] = ItemExame.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('paciente:paciente_detail', kwargs={'pk': self.kwargs['pk']})



class LaudoUpdate(LoginRequiredMixin, UpdateView):
    model = Laudo
    fields = ['paciente_pode_ver', 'medico', 'ultima_menstruacao', 'data_coleta', ]
    template_name = 'laudo/laudo_update.html'

    def form_valid(self, form):
        self.object = form.save()
        item_exames_ids = self.request.POST.getlist("item_exames")
        self.update_laudo_exames(self.object, item_exames_ids)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(LaudoUpdate, self).get_context_data(**kwargs)
        laudo = Laudo.objects.get(pk=self.kwargs['pk'])
        context['laudo'] = laudo
        context['paciente'] = Paciente.objects.get(pk=laudo.paciente.id)
        # Precisa listar todos os exames e itens exames pra dar POST
        context['exames_todos'] = Exame.objects.filter(nome=1)
        items_exame_marcados = ExameLaudo.objects.filter(laudo_id=self.kwargs['pk'])
        context['exame_marcados'] = items_exame_marcados
        exames_feitos = []
        for item in items_exame_marcados:
            exames_feitos.append(item.item_exame.id)
        context['item_exame_todos'] = ItemExame.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('laudo:laudo_detalhe', kwargs={'pk': self.kwargs['pk']})
    
    def update_laudo_exames(self, laudo, item_exames_ids):
        """ Update Exames By Magunun modificado por Leonardo  """
        # deletar tudo e re-criar
        ExameLaudo.objects.filter(laudo_id=laudo.id).delete()
        # salva novos dados
        for item_exame_id in item_exames_ids:
            ExameLaudo.objects.create(laudo=laudo, item_exame_id=item_exame_id)


    
class LaudoAssinatura(LoginRequiredMixin, FormView):
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
        laudo.paciente_pode_ver = True
        laudo.assinado = True
        laudo.data_assinatura = timezone.now()
        laudo.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_context_data(self, **kwargs):
        context = super(LaudoAssinatura, self).get_context_data(**kwargs)
        context['laudo'] = Laudo.objects.get(pk=self.kwargs['pk'])
        context['assinador'] = AssinadorEletronico.objects.filter(user=self.request.user)
        return context
    
    def get_success_url(self):
        laudo = Laudo.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('paciente:paciente_detail', kwargs={'pk': laudo.paciente.id })



def laudos_pendentes(request):
    """ Exibir os laudos pendentes de assinatura/validação. """
    laudos = Laudo.objects.all().filter(assinado=False)
    context = {
        'laudos': laudos
    }
    return render(request, 'laudo/laudos_pendentes.html', context)


def get_tipo_exame_laudo(laudo_id):
    """ Retorna descrição do tipo de exame que é o laudo"""
    exame_laudo = ExameLaudo.objects.filter(laudo_id=laudo_id)[:1]
    id_tipo_exame = 0
    if exame_laudo:
        for item in exame_laudo:
            id_tipo_exame = item.item_exame.exame.nome
    else:
        urina_rotina = ExameUrinaRotina.objects.filter(laudo_id=laudo_id)[:1]
        if urina_rotina:
            id_tipo_exame = 2 #exame urina rotina é 2
    return id_tipo_exame


def get_descricao_tipo_exame_laudo(value):
    for k, v in NOME_EXAME.__iter__():
        if k == value:
            return v

def get_id_tipo_exame_laudo(value):
    for k, v in NOME_EXAME.__iter__():
        if k == value:
            return k


create_laudo = LaudoCreate.as_view() 
laudo_detalhe = LaudoDetail.as_view() 
laudo_update = LaudoUpdate.as_view()
laudo_assinatura = LaudoAssinatura.as_view()