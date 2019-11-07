from django.db import models

# Create your models here.

class User(models.Model):


    SEX = (
        ('0', 'male'),
        ('1', 'female'),
    )

    phonenum = models.CharField(max_length=50, unique=True, verbose_name="手机号")
    nickname = models.CharField(max_length=50, unique=True, verbose_name="昵称")
    sex = models.CharField(max_length=8, choices=SEX, verbose_name="性别")
    birth_year = models.IntegerField(default=2001, verbose_name="出生年")
    birth_month = models.IntegerField(default=1, verbose_name="出生月")
    birth_day = models.IntegerField(default=1, verbose_name="出生日")
    avatar = models.CharField(max_length=50, verbose_name="个人形象")
    location = models.CharField(max_length=50, verbose_name="常居地")
    vip_id = models.IntegerField(default=1, verbose_name="等级")

    class Meta:
        db_table = 'sp_user'


    @property
    def profile(self):

        if not hasattr(self, '_demo'):

            self._demo, _ = Profile.objects.get_or_create(id=self.id)

        return self._demo


# 用户资料模型
class Profile(models.Model):
    SEX = (
        ('0', 'male'),
        ('1', 'female'),
    )

    location = models.CharField(max_length=30, verbose_name="目标城市")
    min_distance = models.IntegerField(default=0, verbose_name="最小查找范围")
    max_distance = models.IntegerField(default=0, verbose_name="最大查找范围")
    min_dating_age = models.IntegerField(default=18, verbose_name="最小交友年龄")
    max_dating_age = models.IntegerField(default=50, verbose_name="最大交友年龄")
    dating_sex = models.CharField(max_length=8, default='0', choices=SEX, verbose_name="匹配的性别")
    vibration = models.BooleanField(default=True, verbose_name="开启震动")
    only_matche = models.BooleanField(default=True, verbose_name="不让为匹配的人看我的相册")
    auto_play = models.BooleanField(default=True, verbose_name="自动播放视频")

    class Meta:
        db_table = 'sp_profile'


