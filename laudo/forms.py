from django import forms
from django.forms.models import inlineformset_factory
from .models import Laudo, ExameLaudo
from medico.models import Medico

class LaudoForm(forms.ModelForm):
    medico = forms.ModelChoiceField(
                queryset=Medico.objects.all(), 
                widget=forms.Select(attrs={'class': 'form-control' }), 
                label='Médico que atendeu',  
                required=True)
    
    class Meta:
        model = Laudo
        exclude = ('data_cadastro', 'data_atualizacao', )


class ExameLaudoForm(forms.ModelForm):
    item_exame = forms.ModelChoiceField(
                    queryset=Medico.objects.all(), 
                    widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control' }), 
                    label='Exames')

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

