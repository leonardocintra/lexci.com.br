from django.contrib import admin
from .models import Laudo, ExameLaudo


class LaudoExameInline(admin.TabularInline):
    model = ExameLaudo

class LaudoAdmin(admin.ModelAdmin):
    fields = ('paciente', 'medico', 'paciente_pode_ver', 'ultima_menstruacao', 'data_coleta', 'ativo', )
    inlines = [LaudoExameInline]

admin.site.register(Laudo, LaudoAdmin)