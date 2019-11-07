import json
import os
import re

from django.conf import settings
from django.forms import model_to_dict
from django.utils.decorators import method_decorator

from common.func import render_json, auth, upload_qiniu
from common import error
from common.func import send_sms_celery
from django_redis import get_redis_connection
from user import models
from django.views import View
from swiper import config

# Create your views here.
# 发送验证码
def send_sms(request):
    # 1、获取参数
    phone = request.POST.get('phone')

    # 2、判断参数
    # 2.1 不能为空
    if not all([phone]):
        return render_json(error.PHONE_NOT_EMPTY, '手机号不能为空')

    # 2.2 格式是否正确
    if not re.match(r'^1[3456789]\d{9}$', phone):
        return render_json(error.PHONE_NOT_FORMAT, '手机号格式不正确')

    # 3、异步执行发送短信的任务
    send_sms_celery.delay(phone)

    return render_json()


# 登陆
def login(request):
    # 1、获取数据
    phone = request.POST.get('phone')
    code = request.POST.get('code')

    # 2、判断数据

    # 获取验证码
    # redis_cli = get_redis_connection()
    # sms_code = redis_cli.get(f'sms_code_{phone}').decode()
    # print(sms_code)


    # TODO 放了测试方便，先注释掉这段代码，上线时一定要打开
    '''
    # 2.0判断验证码是否过期
    if not sms_code:
        return render_json(error.CODE_EXPIRE, '验证码过期')

    # 2.1 判断验证码是否正确
    if sms_code != code:
        return render_json(error.CODE_ERROE, '验证码不正确')


    # 2.2 判断手机号和验证码不能为空
    if not all([phone, code]):
        return render_json(error.PHONE_SMS_NOT_EMPTY, '手机号和验证码不能为空')

    # 2.3 判断手机号的格式
    if not re.match(r'^1[3456789]\d{9}$', phone):
        return render_json(error.PHONE_NOT_FORMAT, '手机号格式不正确')
    '''

    # 3、处理逻辑

    # 逻辑：如果表里面有这个用户，旧直接取出数据，如果没有，直接新增用户数据
    # user = models.User.objects.filter(phonenum=phone).exists()
    # if not user:
    #     models.User.objects.create(phonenum=phone, nickname=phone)

    # 如果有数据那么user就是查出来的对象，created是0
    # 如果没有数据，那么会新增数据，user就是新增数据的对象，created就是1
    user, created = models.User.objects.get_or_create(phonenum=phone, defaults={"nickname": phone})

    # 用session保存用户的数据
    request.session['id'] = user.id

    # 4、返回响应
    return render_json()



# 获取个人资料和修改个人资料
# 如果用类视图，一定套继承View类
# @method_decorator(auth, name='dispatch')
class Profile(View):

    # 类视图访问所有的方法都会先经过dispatch方法
    # @method_decorator(auth)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        # 获取个人资料

        # id = request.session.get('id')
        # user = models.User.objects.get(id=id)
        # profile = user.profile

        # 查处用户资料
        profile = request.user.profile

        # data = {}
        # data['id'] = profile.id
        # data['min_dating_age'] = profile.min_dating_age
        # data['max_dating_age'] = profile.max_dating_age

        # model_to_dict作用是把模型对象转换成字典形式
        return render_json(data=model_to_dict(profile))

    # @method_decorator(auth)
    def put(self, request):
        # 修改个人资料

        # 1、获取参数
        # 用request.body获取put方式传递的参数
        data = request.body
        # 把字节转换成字符串
        data = data.decode()
        # 用json.loads把字符串转成字典
        data = json.loads(data)

        location = data.get('location')
        min_distance = data.get('min_distance')
        max_distance = data.get('max_distance')
        min_dating_age = data.get('min_dating_age')
        max_dating_age = data.get('max_dating_age')
        dating_sex = data.get('dating_sex')

        # 2、判断参数
        # 2.1 判断不为空
        datalist = [location, min_distance, max_distance, min_dating_age, max_dating_age, dating_sex]
        intlist = [min_distance, max_distance, min_dating_age, max_dating_age, dating_sex]


        if not all(datalist):
            return render_json(error.PROFIEL_NOT_EMPTY, '资料不能为空')

        # 2.2 判断距离和年龄要是整型
        # isinstance(a, int)
        if not all([isinstance(i, int) for i in intlist]):
            return render_json(1008, '年龄和距离的类型为int')

        # 2.3 判断最小距离不能大于最大距离
        if min_distance > max_distance:
            return render_json(error.MIN_DIS_NOT_GT_MAX_DIS, 'min_distance > max_distance')


        # 2.4 判断最小年龄不能大于最大年龄
        if min_dating_age > max_dating_age:
            return render_json(error.MIN_AGE_NOT_GT_MAX_AGE, 'min_dating_age > max_dating_age')

        # 3、处理逻辑
        # 把数据更新到数据库
        models.Profile.objects.filter(id=request.user.id).update(
            location=location,
            min_distance=min_distance,
            max_distance=max_distance,
            min_dating_age=min_dating_age,
            max_dating_age=max_dating_age,
            dating_sex=max_dating_age,
        )

        # 4、返回响应
        return render_json(data='修改个人资料成功')


# 上传用户头像
def avater(request):

    # 获取上传图片信息 request.FILES.get('avater')
    file = request.FILES.get('avater')
    # 返回的是一个图片对象，对象的name属性可以返回图片的名字
    filename = file.name

    # 自定义一个文件名称
    new_file_name = 'avater_%s' % request.user.phonenum

    # 获取原文件类型
    name, ext = os.path.splitext(filename)

    # 拼接成新的文件名称
    new_file = new_file_name + ext

    # 上传的本地路径
    filepath = os.path.join(settings.UPLOADS_FIEL, new_file)

    # 把图片上传到uploads目录
    with open(filepath, 'ab') as fp:
        # 分段上传,chunks把上传的文件切成一小段
        for chunk in file.chunks():
            fp.write(chunk)

    # 上传到七牛
    upload_qiniu(new_file, filepath)

    # 七牛的文件地址
    url = config.QN_URL + new_file

    # 把七牛的文件地址保存到数据库
    models.User.objects.filter(id=request.user.id).update(avatar=url)

    return render_json()



