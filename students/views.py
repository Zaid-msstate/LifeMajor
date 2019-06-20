from django.views.generic import TemplateView
from .models import MajorCategory


class AboutView(TemplateView):
    template_name = "students/about.html"


class IndexView(TemplateView):
    template_name = "students/index.html"


class GuideView(TemplateView):
    template_name = "students/guide.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_categories'] = MajorCategory.objects.filter(parent__isnull=True)
        return context
