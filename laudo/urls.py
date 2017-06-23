"""
    Laudo URLs
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.conf.urls import url
from laudo.views import laudo, urina_rotina
from laudo.reports import reports

urlpatterns = [
    # Laudos pendentes de assinatura e revisão
    url(r'^pendentes/$', laudo.laudos_pendentes, name='laudos_pendentes'),
    
    
    url(r'^(?P<pk>[0-9]+)/assinatura/$', laudo.laudo_assinatura, name='laudo_assinatura'),

    # Geracao de Laudo
    # Exame Citopatologico Cervical Uterino
    url(r'^novo/citopatologico-cervical-uterino/(?P<pk_exame>[0-9]+)/paciente/(?P<pk>[0-9]+)/$', laudo.create_laudo, name='create_laudo'),
    url(r'^update/citopatologico-cervical-uterino/(?P<pk>[0-9]+)/$', laudo.laudo_update, name='laudo_update'),

    # Exame Urina Rotia Método Convencional
    url(r'^novo/urina-rotina/(?P<pk_exame>[0-9]+)/paciente/(?P<pk>[0-9]+)/$', urina_rotina.urina_rotina_create, name='urina_rotina_create'),
    url(r'^update/urina-rotina/(?P<pk>[0-9]+)/$', urina_rotina.urina_rotina_update, name='urina_rotina_update'),

    # Detalhe do laudo
    url(r'^detalhe/(?P<pk>[0-9]+)/$', laudo.laudo_detalhe, name='laudo_detalhe'),

    # Imprimir o laudo
    url(r'^imprimir/(?P<laudo_id>[0-9]+)/$', reports.gerar_laudo, name='gerar_laudo'),
]