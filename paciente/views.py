from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView

from .models import Paciente, PacienteEndereco
from .forms import PacienteForm, EnderecoPacienteForm, EnderecoFormSet


class ListPaciente(ListView):
    model = Paciente
    template_name = 'paciente/paciente_list.html'
    context_object_name = 'paciente_list'


class CreatePaciente(CreateView):
    form_class = PacienteForm
    model = Paciente

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        endereco_form = EnderecoFormSet
        return self.render_to_response(self.get_context_data(form=form, endereco_form=endereco_form))
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        endereco_form = EnderecoFormSet(self.request.POST)
        if (form.is_valid() and endereco_form.is_valid()):
            return self.form_valid(form, endereco_form)
        else:
            return self.form_invalid(form, endereco_form)
        
    def form_valid(self, form, endereco_form):
        self.object = form.save()
        endereco_form.instance = self.object
        endereco_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, endereco_form):
        return self.render_to_response(
            self.get_context_data(form=form, endereco_form=endereco_form)
        )
    
    def get_context_data(self, **kwargs):
        kwargs.update({})
        return kwargs
    
    def get_success_url(self):
        return reverse_lazy('paciente:paciente_list')


class UpdatePaciente(UpdateView):
    model = Paciente
    template_name = 'paciente/paciente_update.html'
    fields = ('nome', 'cartao_sus', 'nome_mae', 'apelido', 'cpf', 'nacionalidade', 'data_nascimento', 'raca', 'profissao', 'ativo')

    def get_success_url(self):
        return reverse_lazy('paciente:paciente_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(UpdatePaciente, self).get_context_data(**kwargs)
        context['nome'] = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        context['pk'] = self.kwargs['pk']
        return context


class UpdateEnderecoPaciente(UpdateView):
    model = PacienteEndereco
    template_name = 'paciente/paciente_update.html'
    fields = ('cep', 'logradouro', 'numero_casa', 'complemento', 'bairro', 'uf', 'codigo_municipio', 'municipio', 'ponto_de_referencia', 'fone_ddd', 'fone_numero', 'email')

    def get_success_url(self):
        return reverse_lazy('paciente:paciente_detail', kwargs={'pk': self.object.paciente.pk})
    
    def get_context_data(self, **kwargs):
        context = super(UpdateEnderecoPaciente, self).get_context_data(**kwargs)
        context['nome'] = self.object.paciente.nome
        return context


def create_endereco(request, paciente_id):
    if request.method == "POST":
        form_endereco = EnderecoPacienteForm(request.POST)
        if form_endereco.is_valid():
            endereco = form_endereco.save(commit=False)
            endereco.paciente_id = paciente_id
            endereco.save()
            return redirect('paciente:paciente_detail', pk=paciente_id)
    else:
        context = {
            'form_endereco': EnderecoPacienteForm(),
            'nome': 'colocar o nome aqui',
            'pk': paciente_id
        }
    return render(request, 'paciente/endereco_form.html', context)


def paciente_detail(request, pk):
    form_paciente = get_object_or_404(Paciente, pk=pk)
    try:
        form_endereco = PacienteEndereco.objects.get(paciente_id=pk)
    except PacienteEndereco.DoesNotExist:
        form_endereco = None
    
    context = {
        'form_paciente': form_paciente,
        'form_endereco': form_endereco
    }
    return render(request, 'paciente/paciente_detail.html', context)


paciente_list = ListPaciente.as_view()
paciente_create = CreatePaciente.as_view()
paciente_update = UpdatePaciente.as_view()
endereco_update = UpdateEnderecoPaciente.as_view()