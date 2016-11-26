from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Paciente, PacienteEndereco


class PacienteForm(ModelForm):
    
    class Meta:
        model = Paciente


EnderecoPacienteFormSet = inlineformset_factory(Paciente, PacienteEndereco)