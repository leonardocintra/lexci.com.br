# -*- coding: utf-8 -*-
""" Forms Laudo """
from django import forms
from .models import Laudo, ExameLaudo


class LaudoForm(forms.ModelForm):
    """ LaudoForm - """

    class Meta:
        model = Laudo
        exclude = ('data_cadastro', 'data_atualizacao', 'assinado_por', 'paciente_pode_ver', )

    def create_laudo_exames(self, laudo, item_exames_ids):
        """ Create Laudo By Lucas Magunun """
        for item_exame_id in item_exames_ids:
            ExameLaudo.objects.create(laudo=laudo, item_exame_id=item_exame_id)


class AssinarLaudoEletronicoForm(forms.ModelForm):
    """ Form Assinar Laudo Eletronico """

    class Meta:
        model = Laudo
        fields = ('assinado_por', 'paciente_pode_ver', )


class ExameLaudoForm(forms.ModelForm):
    """ Form utilizado apenas para corrigir/alterar os exames feito pela paciente """

    class Meta:
        model = ExameLaudo
        exclude = ('data_cadastro', )
    
    def update_laudo_exames(self, laudo, item_exames_ids):
        """ Update Exames By Magunun modificado por Leonardo  """
        # deletar tudo e re-criar
        ExameLaudo.objects.filter(laudo_id=laudo.id).delete()
        # salva novos dados
        for item_exame_id in item_exames_ids:
            ExameLaudo.objects.create(laudo=laudo, item_exame_id=item_exame_id)