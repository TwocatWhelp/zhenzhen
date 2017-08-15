# _*_coding:utf-8_*_
from django.contrib import admin
from .models import Post, Category, Tag, Intro
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # 可以在正文中的右侧显示一个过滤栏
    list_filter = ['category', 'tags', 'modified_time']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Intro)
