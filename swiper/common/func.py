import os
import random
import time

from django.conf import settings
from django.http import JsonResponse

from common import error
from swiper import config
import requests
from worker import celery_app
from django_redis import get_redis_connection
from qiniu import Auth, put_file, etag
from vip.models import VipPermRelation, Vip, Permission


def gen_code(num):

    start = 10 ** (num - 1)
    end = 10 ** num - 1

    return random.randint(start, end)


def render_json(code=0, data=None):
    return JsonResponse({'code': code, 'data': data})


@celery_app.task
def send_sms_celery(phone):

    code = gen_code(6)

    param = {
        "sid": config.YZX_SID,
        "token": config.YZX_TOKEN,
        "appid": config.YZX_APP_ID,
        "templateid": config.YXZ_TEMPLATE_ID,
        "param": code,  # 发送的验证码
        "mobile": phone,
    }

    # 发送短信
    res = requests.post(config.YZX_URL, json=param)

    # 获取json格式的数据
    res = res.json()

    # 实例化redis对象
    redis_cli = get_redis_connection()
    # redis_cli.set(f'sms_code_{phone}', code, 180)
    redis_cli.set(f'sms_code_{phone}', code)

    # 4、返回响应
    if res['code'] == '000000':

        return render_json(data='发送验证码成功')
    else:
        return render_json(error.SMS_ERROR, '发送验证码失败')

@celery_app.task
def add(x, y):
    return x * y


def print_info():

    with open(os.path.join(settings.BASE_DIR, 'a.txt'), 'a') as fp:
        fp.write('abcde\n')


# 定义用户登陆权限的装饰器
def auth(func):
    def inner(request, *args, **kwargs):
        if not request.session.get('id'):
            return render_json('1006', '用户未登陆')
        return func(request, *args, **kwargs)
    return inner


# 上传文件到七牛
def upload_qiniu(filename, filepath):

    import qiniu.config
    # 需要填写你的 Access Key 和 Secret Key
    # access_key = config.QN_ACCESS_KEY
    # secret_key = config.QN_SECRET_KEY

    # 构建鉴权对象
    q = Auth(config.QN_ACCESS_KEY, config.QN_SECRET_KEY)
    # 要上传的空间
    bucket_name = config.QN_BUCKET_NAME
    # 上传后保存的文件名
    key = filename
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    # 要上传文件的本地路径
    localfile = filepath
    ret, info = put_file(token, key, localfile)



# 检查权限的装饰器
def check_perm(name):
    def deco(func):
        def inner(request, *args, **kwargs):
            # 1、获取vip_id
            vip_id = request.user.vip_id

            # 2、获取vip_id对应的权限
            pobj = VipPermRelation.objects.filter(vip_id=vip_id)
            pidlist = [p.perm_id for p in pobj]

            # 3、判断传入的权限标示是否在vip_id对应的权限里面
            res = Permission.objects.filter(id__in=pidlist, name=name).exists()

            if not res:
                return render_json(error.NOT_PERSSION, '没有权限')
            else:
                return func(request, *args, **kwargs)

        return inner
    return deco
