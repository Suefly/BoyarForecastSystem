from django.db import models

# Create your models here.


class Test(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    name = models.CharField(max_length=8,verbose_name='名称')
    age = models.IntegerField('年纪',default=22)
    sex = models.CharField(max_length=64,verbose_name='性别',default='wwwwwww')
    remark = models.CharField(max_length=128,verbose_name='备注',default='33333333333333')