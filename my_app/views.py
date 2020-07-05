import random

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from my_app.models import Post


# Create your views here.

def home(request):
    # first_boj = Post.objects.first()
    # last_object = Post.objects.last()
    # count_obj = Post.objects.count()
    # exist_bool = Post.objects.exists()
    # print(first_boj)
    # print(last_object)
    # print(count_obj)
    # print(exist_bool)
    post_list = Post.objects.exclude(title__endswith='5').values_list('id', 'title')

    print(post_list)
    return HttpResponse("Hello Djnago!")


def index(request):
    post_list = Post.objects.all().values("id", "title")
    print(post_list)
    return render(request, 'my_app/index.html', context={"post_list": post_list})


def save_post(request):
    if request.method == "GET":
        return render(request, 'my_app/post_form.html')
    elif request.method == "POST":
        title = request.POST.get("title")
        body = request.POST.get("body")
        Post.objects.create(title=title, body=body)
        return HttpResponse("文章：%s保存成功" % title)


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'my_app/detail.html', context={"post": post})


def update_post(request, id):
    if request.method == "GET":
        post = get_object_or_404(Post, id=id)
        return render(request, "my_app/update.html", context={"post": post})
    elif request.method == "POST":
        new_title = request.POST.get('new_title')
        new_body = request.POST.get('new_body')
        if not id:
            return HttpResponse("请输入文章ID")
        if not new_title and not new_body:
            return HttpResponse("标题和内容不能都为空")
        post = Post.objects.get(id=id)
        if new_title:
            post.title = new_title
        if new_body:
            post.body = new_body
        post.save()
        return HttpResponse("修改成功！")


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return HttpResponse("删除成功！")


def gen_post(request):
    for i in range(100):
        title = "post" + str(random.randrange(100))
        body = "body of " + title
        Post.objects.create(title=title, body=body)
    return HttpResponse("生成了100篇文章！")