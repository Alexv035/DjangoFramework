import json
from datetime import datetime

from django.views.generic import TemplateView
from .models import News

from mainapp import models as mainapp_models
from django.shortcuts import get_object_or_404

# Create your views here.


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):

    template_name = "mainapp/news.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"


class ContactPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"
