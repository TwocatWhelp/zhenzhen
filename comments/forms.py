# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__date__ = '2017/6/21 11:17'
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
