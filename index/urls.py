from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index-index'),
    url(r'^login$', views.user_login, name = 'index-login'),
    url(r'^register$', views.user_register, name = 'index-register'),
    url(r'^logout$', views.user_logout, name = 'index-logout'),
    url(r'^user', views.user, name = 'index-user'),
    url(r'^changepwd', views.change_password, name = 'index-change-pwd'),
    url(r'^invoice', views.change_invoice, name = 'index-change-invoice'),
    url(r'^about$', views.about, name = 'index-about'),
]
