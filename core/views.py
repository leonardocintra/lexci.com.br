from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'core/index.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


index = IndexView.as_view()
about = AboutView.as_view()