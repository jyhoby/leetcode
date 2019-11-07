from django.db import models

# Create your models here.

class Swiped(models.Model):

    MARK = (
        ('like', '喜欢'),
        ('dislike', '不喜欢'),
        ('superlike', '超级喜欢'),
    )
    uid = models.IntegerField(verbose_name="用户自身")
    sid = models.IntegerField(verbose_name="被滑的陌生人")
    mark = models.CharField(max_length=20, choices=MARK, verbose_name="滑动类型")
    time = models.DateTimeField(auto_now_add=True, verbose_name="滑动的时间")

    class Meta:
        db_table = "sp_swiped"


class Friend(models.Model):
    uid1 = models.IntegerField(verbose_name="uid1")
    uid2 = models.IntegerField(verbose_name="uid2")

    class Meta:
        db_table = "sp_friend"
