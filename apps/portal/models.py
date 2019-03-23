from django.contrib.auth.models import User
from django.db import models

# Create your models here.

Use_Flag = (
    (0,'否'),
    (1,'是')
)

class News(models.Model):
    title = models.CharField(max_length=20,verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    create_time = models.DateTimeField(null=True, auto_now_add=True)
    update_time = models.DateTimeField(null=True, auto_now=True)
    class Meta:
        verbose_name_plural = '新闻'

class Introduction(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(null=True, auto_now_add=True)
    update_time = models.DateTimeField(null=True, auto_now=True)
    flag = models.IntegerField(choices=Use_Flag,verbose_name='是否应用',null=True)
    class Meta:
        verbose_name_plural = '关于我们'

class Speech(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(null=True, auto_now_add=True)
    update_time = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        verbose_name_plural = '致辞'

class ContactUs(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    telephone = models.CharField(max_length=20,verbose_name='电话')
    wechat = models.CharField(max_length=20,verbose_name='微信')
    qq = models.CharField(max_length=20, verbose_name='QQ')
    address = models.CharField(max_length=20, verbose_name='地址')
    email = models.CharField(max_length=32,verbose_name='邮箱')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(null=True, auto_now_add=True)
    update_time = models.DateTimeField(null=True, auto_now=True)
    class Meta:
        verbose_name_plural = '联系我们'

class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name='产品名称')
    discription = models.TextField(verbose_name="描述")
    picture = models.ImageField(upload_to='../uploads/',verbose_name="上传图片")
    class Meta:
        verbose_name_plural = '产品展示'
