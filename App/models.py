from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    psw1 = models.CharField(max_length=256)
    user_img = models.CharField(max_length=256)

class Base(models.Model):
    # 图片
    img = models.CharField(max_length=100)
    # 名称
    name = models.CharField(max_length=100)
    # 商品编号
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

class Wheel(Base):
    class Meta:
        db_table = 'xm_wheel'


#################################### 今日推荐单品##########################
class Goods_des(Base):
    # 品牌
    pinpai = models.CharField(max_length=100)
    # 描述
    desc = models.CharField(max_length=100)
    # trackid = models.CharField(max_length=20)
    class Meta:
        db_table = 'goods_des'


class Cart(models.Model):
    # 用户
    user = models.ForeignKey(User)
    # 商品
    goods_des = models.ForeignKey(Goods_des)
    # 商品数量(选择)
    number = models.IntegerField()
    # 是否选中
    isselect = models.BooleanField(default=True)

    class Meta:
        db_table = 'xm_cart'