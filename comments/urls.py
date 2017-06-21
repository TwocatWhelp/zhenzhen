# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__date__ = '2017/6/21 12:59'
from django.conf.urls import url

from . import views


app_name = 'comments'
urlpatterns = [
    url(r'comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]
