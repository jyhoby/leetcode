from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=50, verbose_name="礼物名称")
    price = models.FloatField(default=0, verbose_name="礼物价格")
    stock = models.IntegerField(default=0, verbose_name="礼物库存")
    sales = models.IntegerField(default=0, verbose_name="礼物销量")

    class Meta:
        db_table = 'sp_goods'