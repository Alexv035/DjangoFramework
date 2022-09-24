
from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class MainPageView(TemplateView):
    template_name = 'index.html'


class NewsPageView(TemplateView):
    template_name = 'news.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class ContactPageView(TemplateView):
    template_name = 'contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'doc_site.html'


class CoursesPageView(TemplateView):
    template_name = 'courses_list.html'
