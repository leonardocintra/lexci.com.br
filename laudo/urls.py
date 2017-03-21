from django.conf.urls import url
from . import views, reports

urlpatterns = [
    url(r'^$', views.index, name='laudo_index'),
    url(r'^novo/(?P<pk>[0-9]+)/$', views.create_laudo, name='create_laudo'),
    
    # Exibir detalhes do Laudo
    url(r'^(?P<pk>[0-9]+)/paciente/(?P<paciente_id>[0-9]+)/$', views.laudo_detalhe, name='laudo_detalhe'),
    
    # Imprimir o laudo
    url(r'^(?P<laudo_id>[0-9]+)/paciente/(?P<paciente_id>[0-9]+)/imprimir/$', reports.gerar_laudo, name='gerar_laudo'),

    
    # Exames
    url(r'^exame/$', views.exame_list, name='exame_list'),
    url(r'^exame/novo/$', views.exame_create, name='exame_create'),
    url(r'^exame/delete/(?P<pk>[0-9]+)/$', views.exame_delete, name='exame_delete'),
    url(r'^exame/update/(?P<pk>[0-9]+)/$', views.exame_update, name='exame_update'),
    
    # Exame Itens
    url(r'^exame/item/$', views.item_exame_list, name='item_exame_list'),
    url(r'^exame/(?P<exame_id>[0-9]+)/novo/item/$', views.item_exame_create, name='item_exame_create'),
    url(r'^exame/delete/item/(?P<pk>[0-9]+)/$', views.item_exame_delete, name='item_exame_delete'),
    url(r'^exame/update/item/(?P<pk>[0-9]+)/$', views.item_exame_update, name='item_exame_update'),
]