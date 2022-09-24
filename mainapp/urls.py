from django.urls import path

from mainapp.apps import MainappConfig

from .views import *

app_name = MainappConfig.name

urlpatterns = [
    path('', MainPageView.as_view()),
    path('login/', LoginPageView.as_view()),
    path('doc_site/', DocSitePageView.as_view()),
    path('contacts/', ContactPageView.as_view()),
    path('news/', NewsPageView.as_view()),
    path('courses_list/', CoursesPageView.as_view())
]
