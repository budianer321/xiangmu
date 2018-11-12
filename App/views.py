from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User, Wheel, Goods_des, Cart


def index(request):
    wheels = Wheel.objects.all()
    # print(wheels)

    goods_des = Goods_des.objects.all()

    # 获取cookie
    user_name = request.COOKIES.get('user_name')
    # goods_de = goods_des.first()
    date = {
        'wheels': wheels,
        'goods_des': goods_des,
        'user_name':user_name,
    }
    print(goods_des)
    return render(request, 'index1.html', context=date)


def cart(request):
    user_name = request.COOKIES.get('user_name')
    return render(request,'cart.html')


def goods1(request,goods_des_id):
    goods_des1 = Goods_des.objects.get(id=goods_des_id)

    # goods_des = Goods_des.objects.all()

    date = {
        # 'wheels': wheels,
        # 'goods_des': goods_des,
        # 'user_name': user_name,
        'goods_des1':goods_des1,


    }
    # print(goods_des1.id)
    return render(request,'goods_des.html',context=date)


def goods2(request):

    return render(request,'goods_des2.html')


def login(request):
    if request.method == 'GET':  # 获取登录页面
        return render(request, 'login.html')
    elif request.method == 'POST':  # 登录操作
        # 获取数据
        user_name = request.POST.get('user_name')
        psw1 = request.POST.get('psw1')
        # print(user_name, psw1)

        # 验证
        # 数据库能找到，登录成功
        # 数据库找不到，登录失败
        users = User.objects.filter(user_name=user_name).filter(psw1=psw1)
        if users.count():  # 存在

            user = users.last()
            # print(user.user_name)
        #
            # 重定向首页
            response = redirect('App:index')

            # 设置cookie
            response.set_cookie('user_name', user.user_name)
            print(user.user_name)
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


        # print(user_name, psw1, psw2)


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


def checkaccount(request):
    user_name = request.GET.get('user_name')
    responseData = {
        'msg': '账号可用',
        'status': 1 # 1标识可用，-1标识不可用
    }
    try:
        user = User.objects.get(user_name=user_name)
        responseData['msg'] = '账号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)
    except:
        return JsonResponse(responseData)


def addcart(request):
    user_name = request.COOKIES.get('user_name')
    goodsid = request.GET.get('goodsid')
    # token = request.session.get('token')
    #
    responseData = {
        'msg':'添加购物车成功',
        'status': 1 # 1标识添加成功，0标识添加失败，-1标识未登录
    }
    # return JsonResponse(responseData)
    # if user_name:   # 登录 [直接操作模型]
    #     # 获取用户
    #     user = User.objects.get(user_name=user_name)
    #     # 获取商品
    #     goods_des = Goods_des.objects.get(pk=goodsid)
    #
    #
    #     # 商品已经在购物车，只修改商品个数
    #     # 商品不存在购物车，新建对象（加入一条新的数据）
    #     carts = Cart.objects.filter(user=user).filter(goods_des=goods_des)
    #     if carts.exists():  # 修改数量
    #         cart = carts.first()
    #         cart.number = cart.number + 1
    #         cart.save()
    #         responseData['number'] = cart.number
    #     else:   # 添加一条新记录
    #         cart = Cart()
    #         cart.user = user
    #         cart.goods_des = goods_des
    #         cart.number = 1
    #         cart.save()
    #
    #         responseData['number'] = cart.number
    #
    return JsonResponse(responseData)
    # else:   # 未登录 [跳转到登录页面]
    #     # 由于addcart这个是 用于 ajax操作， 所以这里是不能进行重定向!!
    #     # return redirect('axf:login')
    #     responseData['msg'] = '未登录，请登录后操作'
    #     responseData['status'] = -1
    #     return JsonResponse(responseData)
def subcart(request):
    # 获取数据
    # token = request.session.get('token')
    # goodsid = request.GET.get('goodsid')
    #
    # # 对应用户 和 商品
    # user = User.objects.get(token=token)
    # goods = Goods.objects.get(pk=goodsid)
    #
    # # 删减操作
    # cart = Cart.objects.filter(user=user).filter(goods=goods).first()
    # cart.number = cart.number - 1
    # cart.save()
    #
    responseData = {
        'msg': '购物车减操作成功',
        'status': 1,
        'number': cart.number
    }

    return JsonResponse(responseData)
