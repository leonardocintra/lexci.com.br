from django.contrib import admin
from .models import Laudo, ExameLaudo, AssinadorEletronico


class LaudoExameInline(admin.TabularInline):
    model = ExameLaudo

class LaudoAdmin(admin.ModelAdmin):
    fields = ('paciente', 'medico', 'paciente_pode_ver', 'ultima_menstruacao', 'data_coleta', 'ativo', )
    inlines = [LaudoExameInline]

class AssinadorEletronicoAdmin(admin.ModelAdmin):
    fields = ('nome', )

admin.site.register(Laudo, LaudoAdmin)
admin.site.register(AssinadorEletronico, AssinadorEletronicoAdmin)