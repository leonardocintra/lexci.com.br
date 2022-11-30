"""
    Convenio - Model
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.utils.text import slugify
from .models import Convenio


class ConvenioList(ListView):
    """ Convenio List - Lista os convenios """
    model = Convenio
    template_name = "convenio/convenio_list.html"


class ConvenioCreate(LoginRequiredMixin, CreateView):
    model = Convenio
    fields = ['descricao']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.slup = slugify(form.descricao)
        form.save()


index = ConvenioList.as_view()