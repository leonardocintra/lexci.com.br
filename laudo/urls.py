"""
    Laudo URLs
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.conf.urls import url
from . import views, reports

urlpatterns = [
    url(r'^pendentes/$', views.laudos_pendentes, name='laudos_pendentes'),
    url(r'^novo/paciente/(?P<pk>[0-9]+)/$', views.create_laudo, name='create_laudo'),
    url(r'^(?P<pk>[0-9]+)/$', views.laudo_detalhe, name='laudo_detalhe'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.laudo_update, name='laudo_update'),
    url(r'^(?P<pk>[0-9]+)/update/exames/$', views.exame_laudo_update, name='exame_laudo_update'),
    url(r'^(?P<pk>[0-9]+)/assinatura/$', views.laudo_assinatura, name='laudo_assinatura'),

    # Imprimir o laudo
    url(r'^(?P<laudo_id>[0-9]+)/imprimir/$', reports.gerar_laudo, name='gerar_laudo'),
]