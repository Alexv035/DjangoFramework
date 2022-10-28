import debug_toolbar
from django.conf.urls.static import static
from django.urls import include, path
from django.views.decorators.cache import cache_page

from mainapp import views
from mainapp.apps import MainappConfig

from .views import *

app_name = MainappConfig.name

urlpatterns = [
    path("", MainPageView.as_view(), name="main"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("doc_site/", DocSitePageView.as_view(), name="docs"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("news/", NewsPageView.as_view(), name="news"),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
    path(
        "news/<int:pk>/detail",
        views.NewsDetailView.as_view(),
        name="news_detail",
    ),
    path(
        "news/<int:pk>/update",
        views.NewsUpdateView.as_view(),
        name="news_update",
    ),
    path(
        "news/<int:pk>/delete",
        views.NewsDeleteView.as_view(),
        name="news_delete",
    ),
    path("courses_list/", cache_page(60 * 5)(views.CoursesPageView.as_view()), name="courses"),
    path(
        "courses/<int:pk>/",
        CoursesDetailView.as_view(),
        name="courses_detail",
    ),
    path(
        "course_feedback/",
        views.CourseFeedbackFormProcessView.as_view(),
        name="course_feedback",
    ),
    path("log_view/", views.LogView.as_view(), name="log_view"),
    path("log_download/", views.LogDownloadView.as_view(), name="log_download"),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
