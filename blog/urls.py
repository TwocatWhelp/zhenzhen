# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__date__ = '2017/6/17 10:55'

from django.conf.urls import url

from blog import views

app_name = "blog"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
]
