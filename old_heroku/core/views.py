from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .forms import ContactForm


class IndexView(TemplateView):
    template_name = 'core/index.html'
    

class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send_mail()
        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('contact')


class ManagementView(LoginRequiredMixin, TemplateView):
    template_name = 'core/management.html'


index = IndexView.as_view()
about = AboutView.as_view()
contact = ContactView.as_view()
management = ManagementView.as_view()