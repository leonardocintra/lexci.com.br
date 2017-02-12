from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


class IndexLaudoView(TemplateView):
    """ Laudo Index - Pagina inicial que o usuario cai quando entra no Laudo. """    
    template_name = "laudo/index.html"


class CreateLaudoView(TemplateView):
    # mudar para CreateView
    template_name = 'laudo/laudo_form.html'


index = IndexLaudoView.as_view()
create_laudo = CreateLaudoView.as_view()