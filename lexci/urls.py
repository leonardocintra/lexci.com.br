from django.conf.urls import url
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quem-somos/$', views.about, name='about'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^administrativo/$', views.management, name='management'),
    url(r'^admin/', admin.site.urls),
]
