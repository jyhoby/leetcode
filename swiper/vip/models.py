from django.db import models

# Create your models here.

# vip表
class Vip(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类名称")
    level = models.IntegerField(verbose_name="等级")
    price = models.FloatField(verbose_name="价格")

    class Meta:
        db_table = 'sp_vip'


class Permission(models.Model):
    name = models.CharField(max_length=30, verbose_name="权限名称")
    description = models.CharField(max_length=30, verbose_name="权限说明")

    class Meta:
        db_table = 'db_permission'


class VipPermRelation(models.Model):
    vip_id = models.IntegerField(verbose_name="vipid")
    perm_id = models.IntegerField(verbose_name="权限id")

    class Meta:
        db_table = "sp_vip_perm_relation"