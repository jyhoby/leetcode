from django.db import models


# Create your models here.

class OrderInfo(models.Model):
    uid = models.IntegerField(verbose_name="用户")
    order_code = models.CharField(max_length=100, verbose_name="订单编号")
    total_count = models.IntegerField(default=0, verbose_name="总数量")
    total_amount = models.FloatField(default=0, verbose_name="总金额")
    status = models.SmallIntegerField(default=1, verbose_name="订单状态（1待支付，2待发货、3待签收")

    class Meta:
        db_table = 'sp_order_info'


class OrderDetail(models.Model):
    uid = models.IntegerField(verbose_name="用户id")
    order_code = models.CharField(max_length=100, verbose_name="订单编号")
    goods_id = models.IntegerField(verbose_name="礼物id")
    counts = models.IntegerField(default=0, verbose_name="购买数量")
    price = models.FloatField(default=0, verbose_name="商品单价")

    class Meta:
        db_table = 'sp_order_detail'
