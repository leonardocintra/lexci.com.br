from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.paciente_list, name='paciente_list'),
    url(r'^novo/$', views.paciente_create, name='paciente_create'),
    url(r'^detalhe/(?P<pk>[0-9]+)/$', views.paciente_detail, name='paciente_detail'),	
    url(r'^editar/(?P<pk>[0-9]+)/$', views.paciente_update, name='paciente_update'),
    url(r'^editar/endereco/(?P<pk>[0-9]+)/$', views.endereco_update, name='endereco_update'),
    #url(r'^relatorio/(?P<pk>[0-9]+)/$', reports.paciente_write, name='paciente_relatorio'),
]