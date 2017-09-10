from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.history, name = 'history'),
    url(r'^([0-9]+)$', views.historyitem, name = 'historyitem'),
]
