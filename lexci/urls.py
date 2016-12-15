from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout, login
from core import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quem-somos/$', views.about, name='about'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^administrativo/$', views.management, name='management'),
    url(r'^paciente/', include('paciente.urls', namespace='paciente')),
    url(r'^medico/', include('medico.urls', namespace='medico')),
    url(r'^entrar/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]
