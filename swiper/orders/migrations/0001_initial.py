# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-02 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='用户id')),
                ('order_code', models.CharField(max_length=100, verbose_name='订单编号')),
                ('goods_id', models.IntegerField(verbose_name='礼物id')),
                ('counts', models.IntegerField(default=0, verbose_name='购买数量')),
                ('price', models.FloatField(default=0, verbose_name='商品单价')),
            ],
            options={
                'db_table': 'sp_order_detail',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='用户')),
                ('order_code', models.CharField(max_length=100, verbose_name='订单编号')),
                ('total_count', models.IntegerField(default=0, verbose_name='总数量')),
                ('total_amount', models.FloatField(default=0, verbose_name='总金额')),
                ('status', models.SmallIntegerField(verbose_name='订单状态（1待支付，2待发货、3待签收')),
            ],
            options={
                'db_table': 'sp_order_info',
            },
        ),
    ]
