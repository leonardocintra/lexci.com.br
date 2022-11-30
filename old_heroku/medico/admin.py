"""
    Admin Medico
    Create by: Leonardo Cintra
    Date: Março de 2017
"""
from django.contrib import admin
from .models import Medico

class MedicoAdmin(admin.ModelAdmin):
    """ Cadastro manual de medico """
    exclude = ('data_cadastro', 'data_atualizacao', )


admin.site.register(Medico, MedicoAdmin)