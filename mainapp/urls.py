from django.urls import path

from mainapp.apps import MainappConfig

from .views import *
from mainapp import views

app_name = MainappConfig.name

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("doc_site/", DocSitePageView.as_view(), name="docs"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),

    path("news/", NewsPageView.as_view(), name="news"),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
    path("news/<int:pk>/detail", views.NewsDetailView.as_view(), name="news_detail",),
    path("news/<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update",),
    path("news/<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete",),

    path("courses_list/", CoursesPageView.as_view(), name="courses"),
    path("courses/<int:pk>/", CoursesDetailView.as_view(), name="courses_detail",),
    path("course_feedback/", views.CourseFeedbackFormProcessView.as_view(),
         name="course_feedback",),

]
