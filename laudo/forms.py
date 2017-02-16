from django import forms
from django.forms.models import inlineformset_factory
from .models import Laudo, ExameLaudo

from paciente.models import Paciente


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        exclude =  ('data_cadastro', 'data_atualizacao')


class LaudoForm(forms.ModelForm):

    class Meta:
        model = Laudo
        exclude = ('data_cadastro', 'data_atualizacao', )


class ExameLaudoForm(forms.ModelForm):

    class Meta:
        model = ExameLaudo
        exclude = ('data_cadastro', )
    


PacienteLaudoFormSet = inlineformset_factory(
    Paciente,
    Laudo,    
    can_delete=False,
    fields=('__all__'),
    extra=1
)

ExameLaudoFormSet = inlineformset_factory(
    Laudo,
    ExameLaudo,
    can_delete=False,
    fields=('__all__'),
    extra=1
)

