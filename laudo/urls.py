"""
    Laudo URLs
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""
from django.conf.urls import url
from . import views, reports

urlpatterns = [
    #url(r'^$', views.index, name='laudo_index'),
    url(r'^novo/(?P<pk>[0-9]+)/$', views.create_laudo, name='create_laudo'),

    # Exibir detalhes do Laudo
    url(r'^(?P<pk>[0-9]+)/update/paciente/(?P<paciente_id>[0-9]+)$', views.laudo_update, name='laudo_update'),
    url(r'^(?P<pk>[0-9]+)/paciente/(?P<paciente_id>[0-9]+)/$', views.laudo_detalhe, name='laudo_detalhe'),

    # Imprimir o laudo
    url(r'^(?P<laudo_id>[0-9]+)/paciente/(?P<paciente_id>[0-9]+)/imprimir/$', reports.gerar_laudo, name='gerar_laudo'),
]