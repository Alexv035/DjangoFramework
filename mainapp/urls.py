from django.urls import path

from mainapp.apps import MainappConfig

from .views import *

app_name = MainappConfig.name

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("doc_site/", DocSitePageView.as_view(), name="docs"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("news/", NewsPageView.as_view(), name="news"),
    path("courses_list/", CoursesPageView.as_view(), name="courses"),

    path("news/<int:pk>/", NewsPageDetailView.as_view(), name="news_detail"),
    path("courses/<int:pk>/", CoursesDetailView.as_view(), name="courses_detail",),

]
