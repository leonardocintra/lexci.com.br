""" Exame Admin """
from django.contrib import admin
from .models import Exame, ItemExame, SubExame, SubExameItem

class ExameAdmin(admin.ModelAdmin):
    """ Exame Admin """
    list_display = ('nome', 'descricao', 'ativo', )
    search_fields = ('descricao', )


class ItemExameAdmin(admin.ModelAdmin):
    """ Item Exame Admin """
    list_display = ('descricao_item', 'exame', 'ativo', )

class SubExameAdmin(admin.ModelAdmin):
    """ SubExameAdmin """
    list_display = ('descricao', )


class SubExameItemAdmin(admin.ModelAdmin):
    """ SubExameItemAdmin """
    list_display = ('sub_exame', 'exame', )

admin.site.register(Exame, ExameAdmin)
admin.site.register(ItemExame, ItemExameAdmin)
admin.site.register(SubExame, SubExameAdmin)
admin.site.register(SubExameItem, SubExameItemAdmin)
