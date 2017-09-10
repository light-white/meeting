from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    realname = models.CharField(max_length = 20, verbose_name = u'真实姓名')
    university = models.CharField(max_length = 20, verbose_name = u'学校')
    title = models.CharField(null=True, blank=True, max_length = 20, verbose_name = u'发票抬头')
    invoicenum = models.CharField(null=True, blank=True, max_length = 20, verbose_name = u'纳税人识别号')
    address = models.CharField(null=True, blank=True, max_length = 20, verbose_name = u'快递地址')
    postal = models.CharField(null=True, blank=True, max_length = 20, verbose_name = u'邮政编码')
    phone = models.CharField(null=True, blank=True, max_length = 20, verbose_name = u'手机号')

class Indeximage(models.Model):
    image = models.ImageField(verbose_name = u'图片')
    link = models.CharField(max_length = 100, null=True, blank=True)
    class Meta:
        verbose_name_plural = verbose_name = u'首页图片'
