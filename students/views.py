from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "students/about.html"


class IndexView(TemplateView):
    template_name = "students/index.html"
