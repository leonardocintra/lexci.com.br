from django.contrib import admin
from .models import Exame, ItemExame, Laudo


class ExameAdmin(admin.ModelAdmin):
    fields = ('descricao', )


class ItemExameAdmin(admin.ModelAdmin):
    fields = ('exame', 'descricao_item', )

class LaudoAdmin(admin.ModelAdmin):
    fields = ('paciente', 'medico', 'convenio', 'exames', )


admin.site.register(Exame, ExameAdmin)
admin.site.register(ItemExame, ItemExameAdmin)
admin.site.register(Laudo, LaudoAdmin)