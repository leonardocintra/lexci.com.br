from django import forms
from django.forms.models import inlineformset_factory
from .models import Laudo, ExameLaudo

class LaudoForm(forms.ModelForm):

    class Meta:
        model = Laudo
        exclude = ('data_cadastro', 'data_atualizacao', )


class ExameLaudoForm(forms.ModelForm):

    class Meta:
        model = ExameLaudo
        exclude = ('data_cadastro', )
    
ExameLaudoFormSet = inlineformset_factory(
    Laudo,
    ExameLaudo,
    can_delete=False,
    fields=('__all__'),
    extra=1
)

