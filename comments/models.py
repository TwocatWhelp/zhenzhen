# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'名字')
    email = models.EmailField(max_length=255, verbose_name=u'邮箱')
    url = models.URLField(blank=True, verbose_name=u'网址')
    text = models.TextField()
    # auto_now_add的作用是，当评论数据保存到数据库时，自动把created_time的值指定为当前时间，
    created_time = models.DateTimeField(auto_now_add=True)

    # 这个评论是关联到某篇文章(Post)的，由于一个评论只能属于一篇文章，一篇文章可以有多个评论，是一对多的关系，
    # 因此这里我们使用了ForeignKey.
    post = models.ForeignKey('blog.Post')

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
