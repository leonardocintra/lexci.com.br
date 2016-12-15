from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.medico_list, name='medico_list'),
    url(r'^novo/$', views.medico_create, name='medico_create'),
    url(r'^detalhe/(?P<pk>[0-9]+)/$', views.medico_detail, name='medico_detail'),	
    #url(r'^editar/(?P<pk>[0-9]+)/$', views.medico_update, name='medico_update'),
    #url(r'^relatorio/(?P<pk>[0-9]+)/$', reports.medico_write, name='medico_relatorio'),
]