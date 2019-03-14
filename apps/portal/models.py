from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=20,verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    create_time = models.DateTimeField(null=True, auto_now_add=True)
    update_time = models.DateTimeField(null=True, auto_now=True)
    class Meta:
        verbose_name_plural = '新闻'

