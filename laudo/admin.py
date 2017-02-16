from django.contrib import admin
from .models import Exame, ItemExame, Laudo, ExameLaudo


class ExameAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'ativo', )
    search_fields = ('descricao', )


class ItemExameAdmin(admin.ModelAdmin):
    list_display = ('exame', 'descricao_item', 'ativo', )


class LaudoExameInline(admin.TabularInline):
    model = ExameLaudo

class LaudoAdmin(admin.ModelAdmin):
    fields = ('paciente', 'medico', 'paciente_pode_ver', 'ativo', )
    inlines = [LaudoExameInline]



admin.site.register(Exame, ExameAdmin)
admin.site.register(ItemExame, ItemExameAdmin)
admin.site.register(Laudo, LaudoAdmin)