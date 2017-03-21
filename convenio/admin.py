"""
    Admin Core
    Created by: Leonardo Cintra
    Date: Janeiro de 2017
"""
from django.contrib import admin
from .models import Convenio

class ConvenioAdmin(admin.ModelAdmin):
    """ Cadastro manual de convenio """
    fields = ('descricao', 'slug')
    prepopulated_fields = {'slug': ('descricao', )}


admin.site.register(Convenio, ConvenioAdmin)
