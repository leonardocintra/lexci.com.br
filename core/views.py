from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'core/index.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactView(TemplateView):
    template_name = 'core/contact.html'


class ManagementView(TemplateView):
    template_name = 'core/management.html'


index = IndexView.as_view()
about = AboutView.as_view()
contact = ContactView.as_view()
management = ManagementView.as_view()