"""
    Laudo URLs
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.conf.urls import url
from laudo.views import laudo, urina_rotina
from laudo import reports

urlpatterns = [
    url(r'^pendentes/$', laudo.laudos_pendentes, name='laudos_pendentes'),
    url(r'^novo/paciente/(?P<pk>[0-9]+)/$', laudo.create_laudo, name='create_laudo'),
    url(r'^(?P<pk>[0-9]+)/$', laudo.laudo_detalhe, name='laudo_detalhe'),
    url(r'^(?P<pk>[0-9]+)/update/$', laudo.laudo_update, name='laudo_update'),
    url(r'^(?P<pk>[0-9]+)/assinatura/$', laudo.laudo_assinatura, name='laudo_assinatura'),

    # Imprimir o laudo
    url(r'^(?P<laudo_id>[0-9]+)/imprimir/$', reports.gerar_laudo, name='gerar_laudo'),

    # Exames Urina Rotina
    url(r'^novo/(?P<pk_exame>[0-9]+)/paciente/(?P<pk>[0-9]+)/$', urina_rotina.urina_rotina_create, name='urina_rotina_create'),
]