"""
    Admin Laudo
    Criado por: Leonardo Cintra
    Data: janeiro/2017
"""
from django.contrib import admin
from .models import Laudo, ExameLaudo, AssinadorEletronico, TipoExame


class LaudoExameInline(admin.TabularInline):
    """ Tabular Inlini Laudo"""
    model = ExameLaudo

class LaudoAdmin(admin.ModelAdmin):
    """ Laudo Admin """
    fields = ('paciente', 'medico', 'paciente_pode_ver', 'ultima_menstruacao', 'data_coleta',
              'ativo',)
    inlines = [LaudoExameInline]

class AssinadorEletronicoAdmin(admin.ModelAdmin):
    """ Assinador Eletronico Admin """
    pass

class TipoExameAdmin(admin.ModelAdmin):
    model = TipoExame
    fields = ('descricao', )


admin.site.register(Laudo, LaudoAdmin)
admin.site.register(AssinadorEletronico, AssinadorEletronicoAdmin)
admin.site.register(TipoExame, TipoExameAdmin)
