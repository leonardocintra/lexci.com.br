from django import forms
from django.forms.models import inlineformset_factory
from .models import Paciente, PacienteEndereco


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        exclude = ('data_cadastro', 'data_atualizacao', )

class EnderecoPacienteForm(forms.ModelForm):

    class Meta:
        model = PacienteEndereco
        fields = ('cep', 'logradouro', 'numero_casa', 'complemento', 'bairro', 'uf', 
                  'codigo_municipio', 'municipio', 'fone_ddd', 'fone_numero', 'email', 
                  'ponto_de_referencia' )


EnderecoFormSet = inlineformset_factory(
    Paciente, 
    PacienteEndereco,
    can_delete=False,
    fields=('__all__'),
    extra=1
)