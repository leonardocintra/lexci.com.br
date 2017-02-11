from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


class IndexView(TemplateView):
    """ Laudo Index - Pagina inicial que o usuario cai quando entra no Laudo. """    
    template_name = "laudo/index.html"


class CreateView(CreateView):
    pass
    



index = IndexView.as_view()