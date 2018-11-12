from django.conf.urls import url, include

from App import views

urlpatterns = [
    url(r'^index/$', views.index,name='index'),
    url(r'^cart/$', views.cart,name='cart'),
    url(r'^login/$', views.login,name='login'),
    url(r'^register/$', views.register,name='register'),
    url(r'^goods1/(\d+)/$', views.goods1,name='goods1'),
    url(r'^goods2/$', views.goods2,name='goods2'),

    url(r'^logout/$', views.logout,name='logout'),



    # url(r'^checkaccount/$', views.checkaccount, name='checkaccount'),  #

    url(r'^addcart/$', views.addcart, name='addcart'),  # 添加购物车
    url(r'^subcart/$', views.subcart, name='subcart'),  # 购物车减操作
]