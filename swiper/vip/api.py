import logging

from django.conf import settings
from django.core.mail import send_mail
from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from common.func import render_json
from .models import VipPermRelation, Vip, Permission
from django_redis import get_redis_connection
from user.models import User

def perm(request):

    # 1、获取vip表中所有数据
    vipObj = Vip.objects.all()

    data = []
    for vip in vipObj:

        vpr = VipPermRelation.objects.filter(vip_id=vip.id)

        # 2、查询出vip_id对应的权限id
        plist = [v.perm_id for v in vpr]

        # 3、去权限表中查出对应的权限数据
        pObj = Permission.objects.filter(id__in=plist)

        # 4.1 把对象转换成字典
        vipdict = model_to_dict(vip)
        pDict = [model_to_dict(p) for p in pObj]

        # 4.2 把权限的子对象放入到vip的对象里面
        vipdict['perm'] = pDict

        # 5、把字典放到列表里面
        data.append(vipdict)

    return render_json(data=data)


# 统计全服人气最高的10个用户,从大到小排序
def rank(request):
    # 1、从缓存里面获取HOT_RANk的值
    redis_cli = get_redis_connection('rank')
    data = redis_cli.zrevrange('HOT_RANK', 0, 10, withscores=True)

    # 2、把字节转成整型
    '''
    [(100, 7), (8, 5), (20, -5)]
    '''
    data = [(int(sid), int(socre)) for sid, socre in data]

    # 3、把sid拿出来，去用户表里面查询数据
    '''
    [100, 8, 20]
    '''
    sidlist = [i[0] for i in data]

    # 4、获取user用户的资料
    user = User.objects.filter(id__in=sidlist)
    '''
    [<user 100>, <user 8>, <user 20>]
    '''
    user = sorted(user, key=lambda x: sidlist.index(x.id))

    '''
    [ ((100, 7),<user 100>), ((8, 5),<user 8>), ((20, -5),<user 20>) ]
    '''
    # userdict = [model_to_dict(u) for u in user]
    #
    # for i in range(len(userdict)):
    #     userdict[i]['scroe'] = data[i][1]

    lists = []
    for (sid, score),u in zip(data, user):
        udict = model_to_dict(u)
        udict['score'] = score
        lists.append(udict)


    return render_json(data=lists)



# 发邮件
def mail(request):


    # 保存日志
    err_log = logging.getLogger('inf')

    err_log.error('this is a mail')


    to_email = '290793992zb@163.com'
    verify_url = 'http://www.baidu.com'
    subject = "sz1903"
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                   '<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)

    send_mail(subject, "", settings.EMAIL_FROM, [to_email], html_message=html_message)

    return render_json()