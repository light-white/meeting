from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.meet, name = 'meet'),
    url(r'^([0-9]+)$', views.meetitem, name = 'meetitem'),
    url(r'^joinmeet/([0-9]+)$', views.joinmeet, name = 'joinmeet'),
    url(r'^meetmember/([0-9]+)$', views.meetmember, name = 'meetmember'),
    url(r'^invoicemember/([0-9]+)$', views.invoicemember, name = 'invoicemember'),
]
