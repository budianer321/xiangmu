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
    class Meta:
        db_table = 'goods_des'
