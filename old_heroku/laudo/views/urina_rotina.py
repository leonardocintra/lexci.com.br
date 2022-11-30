"""
    View Urina Rotina
    Criado por Leonardo Cintra
    Data: 13/06/2017
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, FormView, UpdateView

from paciente.models import Paciente
from exame.models import Exame, ItemExame, SubExame, SubExameItem
from laudo.models import Laudo, ExameLaudo, ExameUrinaRotina
from laudo.forms import LaudoForm, ExameUrinaRotinaFormSet, ExameUrinaRotinaForm


class UrinaRotinaCreate(LoginRequiredMixin, FormView):
    """ Gerador do Laudo de Urina Rortina """
    model = Laudo
    template_name = 'laudo/urina_rotina/urina_rotina_form.html'
    form_class = LaudoForm

    def get_initial(self):
        return {
            "paciente" : self.kwargs['pk']
        }
    
    def form_valid(self, form):
        context = self.get_context_data()
        exames_urina_rotina = context['exames_urina_rotina']
        exames = context['exames']
        with transaction.atomic():
            # salva o laudo
            self.object = form.save()
            item_exame = []
            # percorre todos os exames para pegar os dados igual consta no template
            for item in exames:
                item_add = self.request.POST.get('item_{}'.format(item.descricao.replace(" ", "_").lower()))
                if item_add != None:
                    item_exame.append(item_add)
            item_exames_ids = item_exame
            form.create_laudo_exames(self.object, item_exames_ids)
            # salva urina rotina
            if exames_urina_rotina.is_valid():
                exames_urina_rotina.instance = self.object
                exames_urina_rotina.save()
        return HttpResponseRedirect(self.get_success_url())
        
    
    def get_context_data(self, **kwargs):
        context = super(UrinaRotinaCreate, self).get_context_data(**kwargs)
        context['paciente'] = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        exames = Exame.objects.filter(nome=2)
        context['exames'] = exames
        
        # 1 = Caracteristica Fisica | exames é os exames de Urina Rotina (pk=2)
        context['exames_caracteristicas_fisicas'] = get_exames_generic(1, exames)
        context['item_exame_caracteristicas_fisicas'] = get_exames_item_generic(1)
        # 2 = Caracteristica Quimica | exames é os exames de Urina Rotina (pk=2)
        context['exames_caracteristicas_quimicas'] = get_exames_generic(2, exames)
        context['item_exame_caracteristicas_quimicas'] = get_exames_item_generic(2)
        # 3 = Análise microscópica do sedimento | exames é os exames de Urina Rotina (pk=2)
        context['exames_analises_microscopica_do_sedimento'] = get_exames_generic(3, exames)
        context['item_exame_analises_microscopica_do_sedimento'] = get_exames_item_generic(3)

        if self.request.POST:
            context['exames_urina_rotina'] = ExameUrinaRotinaFormSet(self.request.POST)
        else:
            context['exames_urina_rotina'] = ExameUrinaRotinaFormSet()
        return context
    
    def get_success_url(self):
        return reverse_lazy('paciente:paciente_detail', kwargs={'pk': self.kwargs['pk']})


class UrinaRotinaUpdate(LoginRequiredMixin, UpdateView):
    model = Laudo
    fields = ['paciente_pode_ver', 'medico', 'ultima_menstruacao', 'data_coleta', ]
    template_name = 'laudo/urina_rotina/urina_rotina_update.html'

    def form_valid(self, form):
        context = self.get_context_data()
        form_urina_rotina = context['form_urina_rotina']
        exames = context['exames']
        # salva o laudo
        self.object = form.save()
        item_exame = []
        # percorre todos os exames para pegar os dados igual consta no template
        for item in exames:
            item_add = self.request.POST.get('item_{}'.format(item.descricao.replace(" ", "_").lower()))
            if item_add != None:
                item_exame.append(item_add)
        item_exames_ids = item_exame
        self.update_laudo_exames(self.object, item_exames_ids)
        # salva urina rotina
        if form_urina_rotina.is_valid():
            print('--- Graças a Deus ---')
            form_urina_rotina.instance = self.object
            form_urina_rotina.save()
        else:
            print('----- form nao é valido nao sei pq caralio  -------')
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(UrinaRotinaUpdate, self).get_context_data(**kwargs)
        laudo = Laudo.objects.get(pk=self.kwargs['pk'])
        exames = Exame.objects.filter(nome=2)
        items_exame_marcados = ExameLaudo.objects.filter(laudo_id=self.kwargs['pk'])
        context['exames'] = exames
        context['laudo'] = laudo
        context['paciente'] = Paciente.objects.get(pk=laudo.paciente.id)
        context['exames_marcados'] = items_exame_marcados
        # 1 = Caracteristica Fisica | exames é os exames de Urina Rotina (pk=2)
        context['exames_caracteristicas_fisicas'] = get_exames_generic(1, exames)
        context['item_exame_caracteristicas_fisicas'] = get_exames_item_generic(1)
        # 2 = Caracteristica Quimica | exames é os exames de Urina Rotina (pk=2)
        context['exames_caracteristicas_quimicas'] = get_exames_generic(2, exames)
        context['item_exame_caracteristicas_quimicas'] = get_exames_item_generic(2)
        # 3 = Análise microscópica do sedimento | exames é os exames de Urina Rotina (pk=2)
        context['exames_analises_microscopica_do_sedimento'] = get_exames_generic(3, exames)
        context['item_exame_analises_microscopica_do_sedimento'] = get_exames_item_generic(3)
        if self.request.POST:
            context['form_urina_rotina'] = ExameUrinaRotinaFormSet(self.request.POST, instance=self.object)
            context['form_urina_rotina'].full_clean()
        else:
            context['form_urina_rotina'] = ExameUrinaRotinaFormSet(instance=self.object)
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


def get_exames_generic(sub_exame_id, exames):
    """ 
        Retorna uma lista de exames referentes ao sub-item
            - sub_exame_id: id do sub-item
            - exames: lista de exames (nesse caso o nome=2 pois 2 é Urina Rotina)
    """
    subitem_exames = SubExameItem.objects.filter(sub_exame_id=sub_exame_id)
    item_exame = ItemExame.objects.all()
    _return_exames = []
    for exame in exames:
        for sub_item in subitem_exames:
            if sub_item.exame.id == exame.id:
                _return_exames.append(exames.get(pk=exame.id))
    return _return_exames


def get_exames_item_generic(sub_exame_id):
    """
        Retorna uma lista de sub-itens
    """
    subitem_exames = SubExameItem.objects.filter(sub_exame_id=sub_exame_id)
    item_exame = ItemExame.objects.all()
    _return_itens = []
    for item in item_exame:
        for sub_item in subitem_exames:
            if item.exame.id == sub_item.exame.id:
                _return_itens.append(item)
    return _return_itens


urina_rotina_create = UrinaRotinaCreate.as_view()
urina_rotina_update = UrinaRotinaUpdate.as_view()