from django.contrib import admin
from .models import Convenio

class ConvenioAdmin(admin.ModelAdmin):
    fields = ('descricao', 'slug')


admin.site.register(Convenio, ConvenioAdmin)