from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.news, name = 'news'),
    url(r'^([0-9]+)$', views.article, name = 'news-article'),
]
