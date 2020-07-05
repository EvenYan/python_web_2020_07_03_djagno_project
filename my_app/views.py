from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Post


# Create your views here.

def home(request):
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