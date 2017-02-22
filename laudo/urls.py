from django.conf.urls import url
from . import views, reports

urlpatterns = [
    url(r'^$', views.index, name='laudo_index'),
    url(r'^novo/(?P<pk>[0-9]+)/$', views.create_laudo, name='create_laudo'),
    url(r'^laudo/(?P<pk>[0-9]+)/$', reports.gerar_laudo, name='gerar_laudo'),
]