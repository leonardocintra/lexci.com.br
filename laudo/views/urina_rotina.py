"""
    View Urina Rotina
    Criado por Leonardo Cintra
    Data: 13/06/2017
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, FormView

from paciente.models import Paciente
from exame.models import Exame, ItemExame
from laudo.models import Laudo, ExameLaudo, ExameUrinaRotina
from laudo.forms import LaudoForm


class UrinaRotinaDetail(LoginRequiredMixin, DetailView):
    pass

class UrinaRotinaCreate(LoginRequiredMixin, FormView):
    """ Gerador do Laudo de Urina Rortina """
    model = Laudo
    template_name = 'urina_rotina/urina_rotina_form.html'
    form_class = LaudoForm

    def get_initial(self):
        return {
            "paciente" : self.kwargs['pk']
        }
    
    def form_valid(self, form):
        self.object = form.save()
        exames = Exame.objects.filter(nome=2)
        item_exame = []
        # percorre todos os exames para pegar os dados igual consta no template
        for item in exames:
            item_add = self.request.POST.get('item_{}'.format(item.descricao.replace(" ", "_").lower()))
            if item_add != None:
                item_exame.append(item_add)
        item_exames_ids = item_exame
        print(item_exames_ids)
        form.create_laudo_exames(self.object, item_exames_ids)
        return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context = super(UrinaRotinaCreate, self).get_context_data(**kwargs)
        context['paciente'] = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        context['exames'] = Exame.objects.filter(nome=2)
        context['exames_urina'] = ExameUrinaRotina.objects.all()
        context['item_exame'] = ItemExame.objects.all()
        return context
    
    def get_success_url(self):
        return reverse_lazy('paciente:paciente_detail', kwargs={'pk': self.kwargs['pk']})


create_urina_rotina = UrinaRotinaCreate.as_view()