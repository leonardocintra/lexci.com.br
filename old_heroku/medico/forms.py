from django import forms
from .models import Medico


class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico
        exclude ('data_cadastro', 'data_atualizacao', )