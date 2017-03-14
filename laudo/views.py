from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, CreateView, FormView, UpdateView
from django.views.generic.edit import DeleteView

from paciente.models import Paciente
from medico.models import Medico
from .models import Laudo, ItemExame, Exame, ExameLaudo
from .forms import LaudoForm


class IndexLaudoView(TemplateView):
    """ Laudo Index - Pagina inicial que o usuario cai quando entra no Laudo. """    
    template_name = "laudo/index.html"


class CreateLaudoView(FormView):

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
    
    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form)
        )

    def get_context_data(self, **kwargs):
        context = super(CreateLaudoView, self).get_context_data(**kwargs)
        context['paciente'] = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        context['exames'] = Exame.objects.all()
        context['item_exame'] = ItemExame.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('paciente:paciente_detail', kwargs={'pk': self.kwargs['pk']})




class ListExameView(ListView):
    """ Lista os Exames cadastrados """

    model = Exame
    template_name = 'exame/exame_list.html'
    context_object_name = 'exame_list'


class DeleteExameView(DeleteView):
    """ Deleta um exame """

    model = Exame
    template_name = 'exame/exame_confirm_delete.html'
    success_url = reverse_lazy('laudo:exame_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteExameView, self).get_context_data(**kwargs)
        context['items_exame'] = ItemExame.objects.filter(exame=self.kwargs['pk'])
        return context


class UpdateExameView(UpdateView):
    """ Atualiza um exame """

    model = Exame
    fields = ['descricao']
    template_name = 'exame/exame_update_form.html'
    success_url = reverse_lazy('laudo:exame_list')


class ListItemExameView(ListView):
    """ Lista os Itens do Exame """

    model = ItemExame
    template_name = 'exame/item_exame_list.html'
    context_object_name = 'item_exame_list'
    

    def get_context_data(self, **kwargs):
        template_name = 'exame/exame_confirm_delete.html'
        context = super(ListItemExameView, self).get_context_data(**kwargs)
        context['exames'] = Exame.objects.all()
        return context


class UpdateItemExameView(UpdateExameView):
    """ Atualiza um item do exame """

    model = ItemExame
    fields = ['exame', 'descricao_item']
    template_name = 'exame/item_exame_update_form.html'
    success_url = reverse_lazy('laudo:item_exame_list')

    
class DeleteItemExameView(DeleteView):
    """ Deleta o item do exame """

    model = ItemExame
    template_name = 'exame/item_exame_confirm_delete.html'
    success_url = reverse_lazy('laudo:item_exame_list')



index = IndexLaudoView.as_view()
create_laudo = CreateLaudoView.as_view()  
exame_list = ListExameView.as_view()  
exame_delete = DeleteExameView.as_view()
exame_update = UpdateExameView.as_view()
item_exame_list = ListItemExameView.as_view()
item_exame_delete = DeleteItemExameView.as_view()
item_exame_update = UpdateItemExameView.as_view()