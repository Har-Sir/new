#coding=utf8

from __future__ import unicode_literals

from django.db import models

# Create your models here.


#用户表
class user(models.Model):
    U_id = models.AutoField('用户id',primary_key=True)                    #用户id
    U_phone = models.CharField('电话号码',max_length=11)                  #用户号码
    U_name = models.CharField('名字',max_length=50)                       #用户名字
    U_pwd = models.CharField('密码',max_length=50)                        #用户登录密码
    M_sex = models.CharField('性别',max_length=20)                        #用户性别
    U_addr = models.CharField('地址',max_length=100)                      #用户地址(城市)
    U_school = models.CharField('学校',max_length=100)
    # def __str__(self):
    #     return self.name
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'