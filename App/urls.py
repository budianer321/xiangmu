from django.conf.urls import url, include

from App import views

urlpatterns = [
    url(r'^index/$', views.index,name='index'),
    url(r'^cart/$', views.cart,name='cart'),
    url(r'^goods1/$', views.goods1,name='goods1'),
    url(r'^goods2/$', views.goods2,name='goods2'),
    url(r'^login/$', views.login,name='login'),
    url(r'^register/$', views.register,name='register'),

    url(r'^logout/$', views.logout,name='logout'),

    url(r'^logout/$', views.register,name='logout'),


]