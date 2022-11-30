"""
    Convenio URLs
    Criado por: Leonardo Nascimento Cintra
    Data: 21/03/2017
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]