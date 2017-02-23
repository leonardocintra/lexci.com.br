from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView
from .models import Laudo, ItemExame, Exame
from .forms import LaudoForm, ExameLaudoFormSet

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
        exame_form = ExameLaudoFormSet
        return self.render_to_response(
            self.get_context_data(
                form=form,
                exame_form=exame_form
            )
        )
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        exame_form = ExameLaudoFormSet(self.request.POST)

        if (form.is_valid() and exemes_form.is_valid()):
            print('é valido')
            return self.form_valid(form, exame_form)
        else:
            print('num é valido')
            return self.form_invalid(form, exame_form)

    def form_invalid(self, form, exame_form):
        self.object = form.save()
        exame_form.instance = self.object
        exame_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, exame_form):
        return self.render_to_response(
            self.get_context_data(
                form=form, 
                exame_form=exame_form
            )
        )
    
    def get_context_data(self, **kwargs):
        context = super(CreateLaudoView, self).get_context_data(**kwargs)
        context['paciente_id'] = self.kwargs['pk']
        context['paciente'] = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('paciente:paciente_list')
    




index = IndexLaudoView.as_view()
create_laudo = CreateLaudoView.as_view()