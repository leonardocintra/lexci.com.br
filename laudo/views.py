from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView
from .models import Laudo
from .forms import LaudoForm, PacienteLaudoFormSet
from paciente.models import Paciente


class IndexLaudoView(TemplateView):
    """ Laudo Index - Pagina inicial que o usuario cai quando entra no Laudo. """    
    template_name = "laudo/index.html"


class CreateLaudoView(CreateView):
    """ Gerador do Laudo """

    template_name = 'laudo/laudo_form.html'
    form_class = LaudoForm
    model = Laudo

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        paciente_form = PacienteLaudoFormSet
        return self.render_to_response(self.get_context_data(
            form=form,
            paciente_form=paciente_form)
        )
    
    def get_context_data(self, **kwargs):
        context = super(CreateLaudoView, self).get_context_data(**kwargs)
        context['paciente_id'] = self.kwargs['pk']
        context['paciente_obj'] = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        return context

    # TO DO: get_success_url
    




index = IndexLaudoView.as_view()
create_laudo = CreateLaudoView.as_view()