from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User


def index(request):
    # 获取cookie
    user_name = request.COOKIES.get('user_name')

    return render(request, 'index1.html', context={'user_name': user_name})


def cart(request):
    return render(request,'cart.html')


def goods1(request):
    return render(request,'goods_des.html')


def goods2(request):
    return render(request,'goods_des2.html')


def login(request):
    if request.method == 'GET':  # 获取登录页面
        return render(request, 'login.html')
    elif request.method == 'POST':  # 登录操作
        # 获取数据
        user_name = request.POST.get('user_name')
        psw1 = request.POST.get('psw1')
        print(user_name, psw1)

        # 验证
        # 数据库能找到，登录成功
        # 数据库找不到，登录失败
        users = User.objects.filter(user_name=user_name).filter(psw1=psw1)
        if users.count():  # 存在

            user = users.last()
            print(user.user_name)
        #
            # 重定向首页
            response = redirect('App:index')

            # 设置cookie
            response.set_cookie('user_name', user.user_name)

            return response
            # return HttpResponse('登录成功')
        else:  # 不存在
            return HttpResponse('用户名或密码错误!')


    # return render(request,'login.html')


def register(request):
    if request.method == 'GET':  # 获取注册页面
        return render(request, 'register.html')
    elif request.method == 'POST':  # 注册操作
        # 获取客户端传入的数据
        user_name = request.POST.get('user_name')
        psw1 = request.POST.get('psw1')
        psw2 = request.POST.get('psw2')
        # if psw1 != psw2:


        print(user_name, psw1, psw2)


        # 存入数据库
        user = User()
        user.user_name = user_name
        user.psw1 = psw1
        user.save()

        # 重定向首页
        response = redirect('App:index')

        # 状态保持
        response.set_cookie('user_name', user_name)

        # return HttpResponse('注册成功')
        return response

# 退出
def logout(request):
    # print('aaaaaaaaaaaaaa')
    # 重定向首页
    response = redirect('App:index')

    # 删除cookie
    response.delete_cookie('user_name')


    return response
