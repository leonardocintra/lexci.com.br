from django.conf.urls import url
from . import views, reports

urlpatterns = [
    url(r'^$', views.index, name='laudo_index'),
    url(r'^novo/(?P<pk>[0-9]+)/$', views.create_laudo, name='create_laudo'),
    url(r'^paciente/(?P<paciente_id>[0-9]+)/laudo/(?P<laudo_id>[0-9]+)/$', reports.gerar_laudo, name='gerar_laudo'),
    url(r'^exame/$', views.exame_list, name='exame_list'),
    url(r'^exame/item/$', views.item_exame_list, name='item_exame_list'),
]