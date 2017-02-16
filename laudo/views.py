from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView
from .models import Laudo, ItemExame, Exame
from .forms import LaudoForm, PacienteLaudoFormSet, ExameLaudoFormSet

from paciente.models import Paciente
from medico.models import Medico



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
        exames_form = ExameLaudoFormSet
        return self.render_to_response(
            self.get_context_data(
                form=form,
                paciente_form=paciente_form,
                exames_form=exames_form
            )
        )
    
    def post(self, request, *args, **kwargs):
        pass
    
    def get_context_data(self, **kwargs):
        context = super(CreateLaudoView, self).get_context_data(**kwargs)
        context['paciente_id'] = self.kwargs['pk']
        context['paciente'] = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        context['medico'] = Medico.objects.all()
        context['exames'] = Exame.objects.all()
        context['exameItem'] = ItemExame.objects.all()   
        return context

    # TO DO: get_success_url
    




index = IndexLaudoView.as_view()
create_laudo = CreateLaudoView.as_view()