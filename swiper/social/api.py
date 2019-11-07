from django.db.models import Q
from django.forms import model_to_dict
from django.shortcuts import render
import datetime

# 获取推荐列表
from common import error
from common.func import render_json
from user.models import User
from social.models import Swiped, Friend
from django_redis import get_redis_connection
from common.func import check_perm


def get_user(request):
    # 获取当前用户的资料
    profile = request.user.profile

    min_dating_age = profile.min_dating_age
    max_dating_age = profile.max_dating_age
    dating_sex = profile.dating_sex

    # 获取当前时间的年份
    current_year = datetime.date.today().year
    max_birth = current_year - min_dating_age
    min_birth = current_year - max_dating_age

    # 根据条件查询数据表
    # 条件是用户的出生年在max_birth和min_birth之间，而且性别等于dating_sex
    # 条件排除掉喜欢不喜欢超级喜欢的人

    # 先查出划过的用户的id
    swiped = Swiped.objects.filter(uid=request.user.id)
    sidlist = [s.sid for s in swiped]

    user = User.objects.filter(
        birth_year__gt=min_birth,
        birth_year__lt=max_birth,
        sex=dating_sex
    ).exclude(id=request.user.id).exclude(id__in=sidlist)[:20]

    dicts = []
    for u in user:
        dicts.append(model_to_dict(u))

    return render_json(data=dicts)


# 喜欢接口
def like(request):
    uid = request.user.id
    # 获取喜欢的人的ID
    sid = int(request.POST.get('sid'))

    Swiped.objects.create(
        uid=uid,
        sid=sid,
        mark='like'
    )

    # 喜欢加5分
    # 1、创建redis的对象
    redis_cli = get_redis_connection('rank')

    # 2、用哪个方法来减5分 zincrby  -5
    redis_cli.zincrby('HOT_RANK', 5, sid)

    # 判断当前用户喜欢的用户有没有喜欢过我
    res = Swiped.objects.filter(uid=sid, sid=uid, mark__in=['like', 'superlike']).exists()
    if res:
        # 比较两个id的大小，小的赋值给uid1，大的赋值给uid2
        uid1, uid2 = (uid, sid) if uid < sid else (sid, uid)
        Friend.objects.create(uid1=uid1, uid2=uid2)

    return render_json(data='成功')


# 不喜欢
def dislike(request):
    # 获取不喜欢的人的ID
    sid = request.POST.get('sid')

    Swiped.objects.create(
        uid=request.user.id,
        sid=sid,
        mark='dislike'
    )

    # 不喜欢减5分
    # 1、创建redis的对象
    redis_cli = get_redis_connection('rank')

    # 2、用哪个方法来减5分 zincrby  -5
    redis_cli.zincrby('HOT_RANK', -5, sid)

    return render_json(data='成功')


# 超级喜欢
@check_perm('superlike')
def superlike(request):
    uid = request.user.id
    # 获取超级喜欢的人的ID
    sid = int(request.POST.get('sid'))

    Swiped.objects.create(
        uid=uid,
        sid=sid,
        mark='superlike'
    )

    # 超级喜欢加7分
    # 1、创建redis的对象
    redis_cli = get_redis_connection('rank')

    # 2、用哪个方法来减5分 zincrby  -5
    redis_cli.zincrby('HOT_RANK', 7, sid)

    # 判断当前用户喜欢的用户有没有喜欢过我
    res = Swiped.objects.filter(uid=sid, sid=uid, mark__in=['like', 'superlike']).exists()
    if res:
        # 比较两个id的大小，小的赋值给uid1，大的赋值给uid2
        uid1, uid2 = (uid, sid) if uid < sid else (sid, uid)
        Friend.objects.create(uid1=uid1, uid2=uid2)

    return render_json(data='成功')


# 反悔
@check_perm('rewind')
def rewind(request):
    # 连接redis，指定用rewind配置来连接
    redis_cli = get_redis_connection('rewind')

    # 连接redis，指定用rank配置来连接
    rank_cli = get_redis_connection('rank')

    # 用redis来保存反悔的次数，第一次默认为0
    key = 'rewind-%s' % request.user.id
    count = redis_cli.get(key)
    rewind_time = int(count) if count else 0

    if rewind_time < 3:

        now = datetime.datetime.now()
        # 一天的时间 - 当前时间 = 过期时间
        expire_time = 24 * 3600 - now.hour * 3600 - now.minute * 60 - now.second

        # 设置反悔的过期时间
        redis_cli.set(key, rewind_time + 1, expire_time)

        uid = request.user.id
        # 1、找出当前用户上一次划过的用户的id
        # latest
        data = Swiped.objects.filter(uid=uid).latest('time')
        sid = data.sid

        # 反悔的分数和之前喜欢和不喜欢的分数相反
        # if data.mark == 'like':
        #     rank_cli.zincrby('HOT_RANK', -5, sid)
        # elif data.mark == 'superlike':
        #     rank_cli.zincrby('HOT_RANK', -7, sid)
        # elif data.mark == 'dislike':
        #     rank_cli.zincrby('HOT_RANK', 5, sid)

        mark_dict = {'like': -5, 'dislike': 5, 'superlike': -7}
        rank_cli.zincrby('HOT_RANK', mark_dict[data.mark], sid)


        # 2、删除好友关系
        uid1, uid2 = (uid, sid) if uid < sid else (sid, uid)
        res = Friend.objects.filter(uid1=uid1, uid2=uid2).exists()
        if res:
            Friend.objects.filter(uid1=uid1, uid2=uid2).delete()

        # 3、删除滑动记录
        Swiped.objects.filter(uid=uid, sid=sid).delete()

    else:

        return render_json(error.REWIND_COUNT_OVER, '反悔次数到达3次，不允许反悔了')

    return render_json()


# 喜欢我的人
@check_perm('show_liked_me')
def like_me(request):
    swiper = Swiped.objects.filter(sid=request.user.id, mark__in=['like', 'superlike'])

    # lists = []
    # for s in swiper:
    #     lists.append(model_to_dict(s))

    lists = [model_to_dict(s) for s in swiper]

    return render_json(data=lists)


# 查看好友列表
def friend(request):
    uid = request.user.id
    # 判断uid1等于当前用户或者uid2等于当前用户
    friend = Friend.objects.filter(Q(uid1=uid) | Q(uid2=uid))

    # 查出好友的id放入列表里面
    sid = [(f.uid2 if f.uid1 == uid else f.uid1) for f in friend]

    user = User.objects.filter(id__in=sid)

    user = [model_to_dict(u) for u in user]

    return render_json(data=user)
