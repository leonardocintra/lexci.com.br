"""
    View Exame
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from fm.views import AjaxCreateView
from .models import Exame, ItemExame



class IndexExameView(TemplateView):
    """ Exame Index - Pagina inicial que o usuario cai quando entra no Exame. """
    template_name = "exame/index.html"

class ListExameView(ListView):
    """ Lista os Exames cadastrados """

    model = Exame
    template_name = 'exame/exame_list.html'
    context_object_name = 'exame_list'


class CreateExameView(CreateView):
    """ Criar um novo exame """
    model = Exame
    fields = ['descricao']
    template_name = 'exame/exame_form.html'
    success_url = reverse_lazy('exame:exame_list')



class DeleteExameView(DeleteView):
    """ Deleta um exame """

    model = Exame
    template_name = 'exame/exame_confirm_delete.html'
    success_url = reverse_lazy('exame:exame_list')

    def get_context_data(self, **kwargs):
        context = super(DeleteExameView, self).get_context_data(**kwargs)
        context['items_exame'] = ItemExame.objects.filter(exame=self.kwargs['pk'])
        return context


class UpdateExameView(SuccessMessageMixin, UpdateView):
    """ Atualiza um exame """

    model = Exame
    fields = ['descricao']
    template_name = 'exame/exame_update_form.html'
    success_url = reverse_lazy('exame:exame_list')
    success_message = "Exame atualizado com sucesso!"


class ListItemExameView(ListView):
    """ Lista os Itens do Exame """

    model = ItemExame
    template_name = 'exame/item_exame_list.html'
    context_object_name = 'item_exame_list'

    def get_context_data(self, **kwargs):
        context = super(ListItemExameView, self).get_context_data(**kwargs)
        context['exames'] = Exame.objects.all()
        return context


class CreateItemExameView(AjaxCreateView):
    model = ItemExame
    fields = ['exame', 'descricao_item']

    def get_initial(self):
        return {
            "exame" : self.kwargs['exame_id']
        }


class UpdateItemExameView(SuccessMessageMixin, UpdateView):
    """ Atualiza um item do exame """

    model = ItemExame
    fields = ['exame', 'descricao_item']
    template_name = 'exame/item_exame_update_form.html'
    success_url = reverse_lazy('exame:item_exame_list')
    success_message = "Item Exame atualizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super(UpdateItemExameView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class DeleteItemExameView(DeleteView):
    """ Deleta o item do exame """

    model = ItemExame
    template_name = 'exame/item_exame_confirm_delete.html'
    success_url = reverse_lazy('exame:item_exame_list')


index = IndexExameView.as_view()
exame_list = ListExameView.as_view()
exame_create = CreateExameView.as_view()
exame_delete = DeleteExameView.as_view()
exame_update = UpdateExameView.as_view()

item_exame_create = CreateItemExameView.as_view()
item_exame_list = ListItemExameView.as_view()
item_exame_delete = DeleteItemExameView.as_view()
item_exame_update = UpdateItemExameView.as_view()

