from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, FormView

from paciente.models import Paciente
from medico.models import Medico
from .models import Laudo, ItemExame, Exame
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
    

index = IndexLaudoView.as_view()
create_laudo = CreateLaudoView.as_view()    