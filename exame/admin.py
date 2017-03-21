""" Exame Admin """
from django.contrib import admin
from .models import Exame, ItemExame

class ExameAdmin(admin.ModelAdmin):
    """ Exame Admin """
    list_display = ('descricao', 'ativo', )
    search_fields = ('descricao', )


class ItemExameAdmin(admin.ModelAdmin):
    """ Item Exame Admin """
    list_display = ('descricao_item', 'exame', 'ativo', )


admin.site.register(Exame, ExameAdmin)
admin.site.register(ItemExame, ItemExameAdmin)
