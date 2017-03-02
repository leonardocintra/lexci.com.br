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
        form_exame = ExameLaudoFormSet
        return self.render_to_response(
            self.get_context_data(
                form=form,
                form_exame=form_exame
            )
        )
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form_exame = ExameLaudoFormSet(self.request.POST)

        if form.is_valid(): #and exemes_form.is_valid()):
            print('é valido')
            return self.form_valid(form, form_exame)
        else:
            print('num é valido')
            return self.form_invalid(form, form_exame)

    def form_valid(self, form, form_exame):
        self.object = form.save()
        form_exame.instance = self.object
        form_exame.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, form_exame):
        return self.render_to_response(
            self.get_context_data(
                form=form, 
                form_exame=form_exame
            )
        )
    
    def get_context_data(self, **kwargs):
        context = super(CreateLaudoView, self).get_context_data(**kwargs)
        context['paciente_id'] = self.kwargs['pk']
        context['paciente'] = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        context['exames'] = Exame.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('paciente:paciente_list')
    

index = IndexLaudoView.as_view()
create_laudo = CreateLaudoView.as_view()