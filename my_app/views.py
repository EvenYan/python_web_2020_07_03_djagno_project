import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Max, Min, Count, Avg, Sum, F, Q
from django.urls import reverse

from my_app.models import Post, Score, UserInfo


# Create your views here.

def home(request):
    name = request.session.get('user')
    # print("request encoding" + str(request.encoding))
    # print("request post" + str(request.POST))
    # print("request get" + str(request.GET))
    # print("request method" + str(request.method))
    # print("request path" + str(request.path))
    # print("request cookies" + str(request.COOKIES))
    # print("request session" + str(request.session))
    # print(request.is_ajax())
    # print(request.get_host())

    # first_boj = Post.objects.first()
    # last_object = Post.objects.last()
    # count_obj = Post.objects.count()
    # exist_bool = Post.objects.exists()
    # print(first_boj)
    # print(last_object)
    # print(count_obj)
    # print(exist_bool)
    # student = Score.objects.filter(~Q(math__gte=90)).values("name", "math", "chinese")
    # print(student)
    # a = 10/0
    request.session.flush()
    return HttpResponse("欢迎您 %s!" %name)


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


def gen_score(request):
    for i in range(100):
        name = "Student" + str(random.randrange(100))
        math = random.randrange(50, 100)
        chinese = random.randrange(40, 90)
        Score.objects.create(name=name, math=math, chinese=chinese)
    return HttpResponse("生成了100个学生的成绩！")


def get_form(request):
    if request.method == "GET":
        resp = render(request, 'my_app/form.html')
        print(resp.content)
        print(resp.charset)
        print(resp)
        resp.write("Hello Word")
        return resp
        # return redirect(reverse('my:detail', args=(5, )))
    elif request.method == "POST":
        name = request.POST.get('name')
        passwd = request.POST.get('passwd')
        request.session['user'] = name
        request.session.set_expiry(60)
        print(name)
        print(passwd)
        resp = HttpResponse(("注册成功！"))
        # resp.set_cookie('name', name, max_age=30)
        return resp


def template_demo(request):
    people_dict = {"name": 'Even', "age": "10"}
    data_list = [1, 2, 4, 5, 6]
    return render(request, 'my_app/my_page.html', context={"people_info": people_dict, 'data_list': data_list})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        email = request.POST.get('email')
        confirm_passwd = request.POST.get("passwd_confirm")
        print(username, email, passwd, confirm_passwd)
        if not username and not email and not passwd and not confirm_passwd:
            return HttpResponse("请检查是否漏填")
        if passwd == confirm_passwd:
            from my_app.tools import gen_secret
            passwd = gen_secret(passwd)
            request.session['username'] = username
            UserInfo.objects.create(username=username, email=email, passwd=passwd)
            return render(request, 'my_app/register.html')
        return HttpResponse("密码不一致，请重新注册！")
    return render(request, "my_app/register.html")


def login(request):
    username = request.POST.get('username')
    passwd = request.POST.get('passwd')
    session_username = request.session.get('username')
    print(username, passwd, session_username)
    if username == session_username:
        from my_app.tools import gen_secret
        passwd = gen_secret(passwd)
        db_passwd = UserInfo.objects.filter(username=username)[0].passwd
        print(db_passwd)
        if passwd == db_passwd:
            return render(request, 'my_app/user_center.html', context={'username': username})
        return HttpResponse("账号或密码有误，请重新输入")
    return HttpResponse("账号或密码有误，请重新输入！")


def logout(request):
    request.session.flush()
    username = request.session.get("username")
    print(username)
    return render(request, 'my_app/user_center.html', context={'username': username})