#coding=utf8

from __future__ import unicode_literals

from django.db import models

# Create your models here.

#管理员表
class manager(models.Model):
    M_id = models.IntegerField('管理员编号',primary_key=True)
    M_name = models.CharField('名字',max_length=50)
    M_pwd = models.CharField('密码',max_length=50)
    M_sex = models.CharField('性别',max_length=20)
    M_phone = models.CharField('电话',max_length=11)
    M_type = models.CharField('权限',max_length=20)
    # class Meta:
    #     db_table = "manager"
    class Meta:
        verbose_name = '管理员信息'
        verbose_name_plural = '管理员信息'

#用户表
class user(models.Model):
    U_id = models.AutoField('用户id',primary_key=True)
    U_phone = models.CharField('电话号码',max_length=11)
    U_name = models.CharField('名字',max_length=50)
    U_pwd = models.CharField('密码',max_length=50)
    M_sex = models.CharField('性别',max_length=20)
    U_addr = models.CharField('地址',max_length=100)
    U_school = models.CharField('学校',max_length=100)
    # def __str__(self):
    #     return self.name
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


#车次表
class train(models.Model):
    T_id = models.CharField('车次编号',max_length=20,primary_key=True)
    T_name = models.CharField('车次名',max_length=50)
    R_id = models.CharField('路线编号',max_length=20)
    T_starttime = models.DateTimeField('出发时间',max_length=50)
    T_arrttime = models.DateTimeField('到达时间',max_length=50)
    T_price = models.FloatField('单价', max_length=50)
    T_num = models.IntegerField('车票数量')
    T_yp = models.IntegerField('余票')
    T_car = models.CharField('车牌号', max_length=20)
    class Meta:
        verbose_name = '车次信息'
        verbose_name_plural = '车次信息'

#路线
class route(models.Model):
    R_id = models.CharField('路线编号',max_length=20, primary_key=True)
    R_startcity = models.CharField('起始城市',max_length=50)
    R_arrtcity = models.CharField('目的城市',max_length=50)
    R_startplace = models.CharField('上车点',max_length=50)
    R_arrtplace = models.CharField('下车点',max_length=50)
    class Meta:
        verbose_name = '路线信息'
        verbose_name_plural = '路线信息'

#订单
class order(models.Model):
    O_id = models.AutoField('订单编号',primary_key=True)
    U_id = models.IntegerField('用户id')
    T_id = models.IntegerField('车次编号')
    O_num = models.IntegerField('购买数量')
    O_totalpri = models.FloatField('总价', max_length=50)
    O_orderstates = models.CharField('订单状态',max_length=20)
    O_paystates = models.CharField('付款状态',max_length=20)
    O_paymode = models.CharField('付款方式',max_length=20)
    O_ordertime = models.DateTimeField('下单时间',max_length=50)
    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = '订单信息'

#意见反馈
class suggestion(models.Model):
    SU_id = models.AutoField('意见id',primary_key=True)
    U_id = models.IntegerField('用户id')
    SU_time = models.DateTimeField('反馈时间',max_length=50)
    SU_content = models.CharField('内容',max_length=150)
    class Meta:
        verbose_name = '意见反馈'
        verbose_name_plural = '意见反馈'

#车讯
class inform(models.Model):
    I_id = models.AutoField('车讯id',primary_key=True)
    T_id = models.CharField('车次编号',max_length=20)
    I_content = models.CharField('内容',max_length=150)
    class Meta:
        verbose_name = '车讯信息'
        verbose_name_plural = '车讯信息'

#帮助信息
class help(models.Model):
    H_id = models.AutoField('车讯id',primary_key=True)
    H_content = models.CharField('内容',max_length=150)
    class Meta:
        verbose_name = '车讯信息'
        verbose_name_plural = '车讯信息'
