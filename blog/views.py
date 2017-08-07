# _*_ coding: utf-8 _*_
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Intro, Category
from comments.forms import CommentForm
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import EmailPostForm

import markdown
# Create your views here.


def detail(request, pk):
    intro = Intro.objects.all()
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    return render(request, 'article.html', context={'post': post,
                                                    'intro': intro,
                                                    'form': form,
                                                    'comment_list': comment_list})


# 文章列表
def index(request):
    # order_by()方法作用是可以进行排序
    post_list = Post.objects.all().order_by('-created_time')
    intro = Intro.objects.all()
    return render(request, 'index.html', context={'post_list': post_list,
                                                  'intro': intro})


# 分类下文章列表
def archives(request, year, month):
    intro = Intro.objects.all()
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list,
                                                  'intro': intro})


# 归档下文章列表
def category(request, pk):
    intro = Intro.objects.all()
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list,
                                                  'intro': intro
                                                  })


# email验证发送
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # 如果表单数据验证通过，我们通过访问form.cleaned_data获取验证过的数据，这个属性是一个表单字段和值得字典
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'zzl_wen@sina.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'share.html', {'post': post,
                                          'form': form,
                                          'sent': sent})
