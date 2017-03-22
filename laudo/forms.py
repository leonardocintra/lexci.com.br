# -*- coding: utf-8 -*-
""" Forms Laudo """
from django import forms
from .models import Laudo, ExameLaudo


class LaudoForm(forms.ModelForm):
    """ LaudoForm - """
    
    class Meta:
        model = Laudo
        exclude = ('data_cadastro', 'data_atualizacao', 'assinado_por', )

    
    def create_laudo_exames(self, laudo, item_exames_ids):
        for item_exame_id in item_exames_ids:
            ExameLaudo.objects.create(laudo=laudo, item_exame_id=item_exame_id)