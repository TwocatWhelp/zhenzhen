# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__date__ = '2017/7/19 8:48'

from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
    # 设置required=False让comments的字段可选，可有可无，widget=forms.Textarea是让在html中以<textarea><textarea>元素显示。
