from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse('欢迎使用')

def user_list(request):
    # 默认情况下回去这个父级文件夹寻找user_list.html,有些情况是优先根目录
    return render(request, "user_list.html")

def user_add(request):
    return render(request, "user_add.html")

def tpl(request):
    name = '蜡笔小新'
    role = ["管理员", "CEO", "保安"]
    user_info = {"name": "蜡笔小新", "salary": 2444, "role": "CEO"}
    return render(request, 'tpl.html', {"n1": name, "n2": role, "n3": user_info})

def news(request):

    # 定义一些新闻 或 去数据库  网络请求：https://www.gov.cn/yaowen/liebiao/202603/content_7060929.htm
    # 第三方模块：requests (pip install requests)
    import requests
    res = requests.get("https://api.quotable.io/random")
    data_list = res.json()
    print(data_list)
    return render(request, 'news.html', {"news_list": data_list})

def something(request):
    # request是一个对象，封装了用户发送过来的所有请求相关的数据

    # 1. 获取请求的方式 GET/POST
    print(request.method)

    # 2.在URL是传递以一些值
    print(request.GET)

    # 3.在请求体中传递数据
    print(request.POST)

    # 4.内容字符串1返回内容给请求者
    # return HttpResponse("返回内容")

    # 5.读取HTML内容+渲染（替换） -》 字符串，返回给用户浏览器
    #　return render(request, 'something.html', {"title": "来了"})

    # 6.【响应】让浏览器重定向
    return redirect("https://www.baidu.com")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # print(request.POST)
        # return HttpResponse("登入成功")
        username = request.POST.get('user')
        password = request.POST.get('pwd')
    if username == 'root' and password == '123':
        # return HttpResponse("登入成功")
        return redirect("https://www.bilibili.com/")
    else:
        return render(request, 'login.html', {'error_msg': "用户或密码错误"})
    
from app01.models import Department, UserInfo
def orm(request):
    Department.objects.create(title="销售部")
    Department.objects.create(title="ID部")
    return HttpResponse("成功")