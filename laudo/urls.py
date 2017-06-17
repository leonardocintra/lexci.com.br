"""
    Laudo URLs
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.conf.urls import url
from laudo.views import laudo, urina_rotina
from laudo.reports import reports, report_urina_rotina

urlpatterns = [
    # Laudos pendentes de assinatura e revisão
    url(r'^pendentes/$', laudo.laudos_pendentes, name='laudos_pendentes'),
    
    url(r'^update/(?P<pk>[0-9]+)/$', laudo.laudo_update, name='laudo_update'),
    url(r'^(?P<pk>[0-9]+)/assinatura/$', laudo.laudo_assinatura, name='laudo_assinatura'),

    # Geracao de Laudo
    url(r'^novo/citopatologico-cervical-uterino/(?P<pk_exame>[0-9]+)/paciente/(?P<pk>[0-9]+)/$', laudo.create_laudo, name='create_laudo'),
    url(r'^novo/urina-rotina/(?P<pk_exame>[0-9]+)/paciente/(?P<pk>[0-9]+)/$', urina_rotina.urina_rotina_create, name='urina_rotina_create'),

    # Detalhe do laudo
    url(r'^detalhe/(?P<pk>[0-9]+)/$', laudo.laudo_detalhe, name='laudo_detalhe'),

    # Imprimir o laudo
    url(r'^imprimir/citopatologico-cervical-uterino/(?P<laudo_id>[0-9]+)/$', reports.gerar_laudo, name='gerar_laudo'),
    url(r'^imprimir/urina-rotina/(?P<laudo_id>[0-9]+)/$', report_urina_rotina.gerar_laudo_urina_rotina, name='gerar_laudo_urina_rotina'),
]