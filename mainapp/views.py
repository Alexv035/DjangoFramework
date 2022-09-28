import json
from datetime import datetime

from django.views.generic import TemplateView

# Create your views here.


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # with open("news.json") as f:
        #     data = json.load(f)
        # context['news'] = data['news']
        # context['news_date'] = datetime.now()
        # context['range'] = len(data['news'])

        context["news_title"] = "Новость"
        context["description"] = "Предварительное описание новости"
        context["news_date"] = datetime.now()
        context["range"] = range(5)

        return context


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"


class ContactPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"
