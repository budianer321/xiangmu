from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'index1.html')


def cart(request):
    return render(request,'cart.html')


def goods1(request):
    return render(request,'goods_des.html')


def goods2(request):
    return render(request,'goods_des2.html')


def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')