"""
    Exame URLs
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""

from django.conf.urls import url
from . import views

urlpatterns = [

    # Exames
    url(r'^gerenciamento/$', views.index, name='index'),
    url(r'^$', views.exame_list, name='exame_list'),
    url(r'^novo/$', views.exame_create, name='exame_create'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.exame_delete, name='exame_delete'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.exame_update, name='exame_update'),

    # Exame Itens
    url(r'^item/$', views.item_exame_list, name='item_exame_list'),
    url(r'^item/(?P<exame_id>[0-9]+)/novo/$', views.item_exame_create, name='item_exame_create'),
    url(r'^item/(?P<pk>[0-9]+)/delete/$', views.item_exame_delete, name='item_exame_delete'),
    url(r'^item/(?P<pk>[0-9]+)/update/$', views.item_exame_update, name='item_exame_update'),
]