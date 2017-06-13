"""
    View Exame
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from fm.views import AjaxCreateView
from .models import TipoExame, ItemExame



class ExameIndex(LoginRequiredMixin, TemplateView):
    """ Exame Index - Pagina inicial que o usuario cai quando entra no TipoExame. """
    template_name = "exame/index.html"

class TipoExameList(LoginRequiredMixin, ListView):
    """ Lista os Exames cadastrados """

    model = TipoExame
    template_name = 'exame/exame_list.html'
    context_object_name = 'exame_list'


class TipoExameCreate(LoginRequiredMixin, CreateView):
    """ Criar um novo exame """
    model = TipoExame
    fields = ['descricao']
    template_name = 'exame/exame_form.html'
    success_url = reverse_lazy('exame:exame_list')



class TipoExameDelete(LoginRequiredMixin, DeleteView):
    """ Deleta um exame """

    model = TipoExame
    template_name = 'exame/exame_confirm_delete.html'
    success_url = reverse_lazy('exame:exame_list')

    def get_context_data(self, **kwargs):
        context = super(TipoExameDelete, self).get_context_data(**kwargs)
        context['items_exame'] = ItemExame.objects.filter(exame=self.kwargs['pk'])
        return context


class TipoExameUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ Atualiza um exame """

    model = TipoExame
    fields = ['descricao', 'ordem_exibicao', ]
    template_name = 'exame/exame_update_form.html'
    success_url = reverse_lazy('exame:exame_list')
    success_message = "Exame atualizado com sucesso!"


class ItemExameList(LoginRequiredMixin, ListView):
    """ Lista os Itens do Exame """

    model = ItemExame
    template_name = 'exame/item_exame_list.html'
    context_object_name = 'item_exame_list'

    def get_context_data(self, **kwargs):
        context = super(ItemExameList, self).get_context_data(**kwargs)
        context['exames'] = TipoExame.objects.all()
        return context


class ItemExameCreate(AjaxCreateView):
    model = ItemExame
    fields = ['exame', 'descricao_item']

    def get_initial(self):
        return {
            "exame" : self.kwargs['exame_id']
        }


class ItemExameUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ Atualiza um item do exame """

    model = ItemExame
    fields = ['exame', 'descricao_item']
    template_name = 'exame/item_exame_update_form.html'
    success_url = reverse_lazy('exame:item_exame_list')
    success_message = "Item Exame atualizado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super(ItemExameUpdate, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context


class ItemExameDelete(LoginRequiredMixin, DeleteView):
    """ Deleta o item do exame """

    model = ItemExame
    template_name = 'exame/item_exame_confirm_delete.html'
    success_url = reverse_lazy('exame:item_exame_list')


index = ExameIndex.as_view()
exame_list = TipoExameList.as_view()
exame_create = TipoExameCreate.as_view()
exame_delete = TipoExameDelete.as_view()
exame_update = TipoExameUpdate.as_view()

item_exame_create = ItemExameCreate.as_view()
item_exame_list = ItemExameList.as_view()
item_exame_delete = ItemExameDelete.as_view()
item_exame_update = ItemExameUpdate.as_view()

