# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-06 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='help',
            fields=[
                ('H_id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u8f66\u8bafid')),
                ('H_content', models.CharField(max_length=150, verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u8f66\u8baf\u4fe1\u606f',
                'verbose_name_plural': '\u8f66\u8baf\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='inform',
            fields=[
                ('I_id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u8f66\u8bafid')),
                ('T_id', models.CharField(max_length=20, verbose_name='\u8f66\u6b21\u7f16\u53f7')),
                ('I_content', models.CharField(max_length=150, verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u8f66\u8baf\u4fe1\u606f',
                'verbose_name_plural': '\u8f66\u8baf\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('M_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u7ba1\u7406\u5458\u7f16\u53f7')),
                ('M_name', models.CharField(max_length=50, verbose_name='\u540d\u5b57')),
                ('M_pwd', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
                ('M_sex', models.CharField(max_length=20, verbose_name='\u6027\u522b')),
                ('M_phone', models.CharField(max_length=11, verbose_name='\u7535\u8bdd')),
                ('M_type', models.CharField(max_length=20, verbose_name='\u6743\u9650')),
            ],
            options={
                'verbose_name': '\u7ba1\u7406\u5458\u4fe1\u606f',
                'verbose_name_plural': '\u7ba1\u7406\u5458\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('O_id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u8ba2\u5355\u7f16\u53f7')),
                ('U_id', models.IntegerField(verbose_name='\u7528\u6237id')),
                ('T_id', models.IntegerField(verbose_name='\u8f66\u6b21\u7f16\u53f7')),
                ('O_num', models.IntegerField(verbose_name='\u8d2d\u4e70\u6570\u91cf')),
                ('O_totalpri', models.FloatField(max_length=50, verbose_name='\u603b\u4ef7')),
                ('O_orderstates', models.CharField(max_length=20, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('O_paystates', models.CharField(max_length=20, verbose_name='\u4ed8\u6b3e\u72b6\u6001')),
                ('O_paymode', models.CharField(max_length=20, verbose_name='\u4ed8\u6b3e\u65b9\u5f0f')),
                ('O_ordertime', models.DateTimeField(max_length=50, verbose_name='\u4e0b\u5355\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u4fe1\u606f',
                'verbose_name_plural': '\u8ba2\u5355\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='route',
            fields=[
                ('R_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='\u8def\u7ebf\u7f16\u53f7')),
                ('R_startcity', models.CharField(max_length=50, verbose_name='\u8d77\u59cb\u57ce\u5e02')),
                ('R_arrtcity', models.CharField(max_length=50, verbose_name='\u76ee\u7684\u57ce\u5e02')),
                ('R_startplace', models.CharField(max_length=50, verbose_name='\u4e0a\u8f66\u70b9')),
                ('R_arrtplace', models.CharField(max_length=50, verbose_name='\u4e0b\u8f66\u70b9')),
            ],
            options={
                'verbose_name': '\u8def\u7ebf\u4fe1\u606f',
                'verbose_name_plural': '\u8def\u7ebf\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='suggestion',
            fields=[
                ('SU_id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u610f\u89c1id')),
                ('U_id', models.IntegerField(verbose_name='\u7528\u6237id')),
                ('SU_time', models.DateTimeField(max_length=50, verbose_name='\u53cd\u9988\u65f6\u95f4')),
                ('SU_content', models.CharField(max_length=150, verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u610f\u89c1\u53cd\u9988',
                'verbose_name_plural': '\u610f\u89c1\u53cd\u9988',
            },
        ),
        migrations.CreateModel(
            name='train',
            fields=[
                ('T_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='\u8f66\u6b21\u7f16\u53f7')),
                ('T_name', models.CharField(max_length=50, verbose_name='\u8f66\u6b21\u540d')),
                ('R_id', models.CharField(max_length=20, verbose_name='\u8def\u7ebf\u7f16\u53f7')),
                ('T_starttime', models.DateTimeField(max_length=50, verbose_name='\u51fa\u53d1\u65f6\u95f4')),
                ('T_arrttime', models.DateTimeField(max_length=50, verbose_name='\u5230\u8fbe\u65f6\u95f4')),
                ('T_price', models.FloatField(max_length=50, verbose_name='\u5355\u4ef7')),
                ('T_num', models.IntegerField(verbose_name='\u8f66\u7968\u6570\u91cf')),
                ('T_yp', models.IntegerField(verbose_name='\u4f59\u7968')),
                ('T_car', models.CharField(max_length=20, verbose_name='\u8f66\u724c\u53f7')),
            ],
            options={
                'verbose_name': '\u8f66\u6b21\u4fe1\u606f',
                'verbose_name_plural': '\u8f66\u6b21\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('U_id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u7528\u6237id')),
                ('U_phone', models.CharField(max_length=11, verbose_name='\u7535\u8bdd\u53f7\u7801')),
                ('U_name', models.CharField(max_length=50, verbose_name='\u540d\u5b57')),
                ('U_pwd', models.CharField(max_length=50, verbose_name='\u5bc6\u7801')),
                ('M_sex', models.CharField(max_length=20, verbose_name='\u6027\u522b')),
                ('U_addr', models.CharField(max_length=100, verbose_name='\u5730\u5740')),
                ('U_school', models.CharField(max_length=100, verbose_name='\u5b66\u6821')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
    ]
