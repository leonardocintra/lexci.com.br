""" Exame Admin """
from django.contrib import admin
from .models import TipoExame, ItemExame

class TipoExameAdmin(admin.ModelAdmin):
    """ TipoExame Admin """
    list_display = ('descricao', 'ativo', )
    search_fields = ('descricao', )


class ItemExameAdmin(admin.ModelAdmin):
    """ Item Exame Admin """
    list_display = ('descricao_item', 'exame', 'ativo', )


admin.site.register(TipoExame, TipoExameAdmin)
admin.site.register(ItemExame, ItemExameAdmin)
