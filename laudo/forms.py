from django import forms
from .models import Laudo, ItemExame, Exame, ExameLaudo


class LaudoForm(forms.ModelForm):

    class Meta:
        model = Laudo
        exclude = ('data_cadastro', 'data_atualizacao', )