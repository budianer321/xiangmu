from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    psw1 = models.CharField(max_length=256)
    user_img = models.CharField(max_length=256)

class Wheel(models.Model):
    # 图片
    img = models.CharField(max_length=100)
    # 名称
    name = models.CharField(max_length=100)
    # 商品编号
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True
        db_table = 'xm_wheel'