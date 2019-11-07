import os

from alipay import AliPay
from django.conf import settings
from django.db import transaction
from django.shortcuts import render, redirect
import json
import datetime

from common import error
from common.func import render_json
from .models import OrderDetail, OrderInfo
from goods.models import Goods


def commits(request):
    # 1、获取数据
    info = request.POST.get('info')

    # 2、转成字典
    info = json.loads(info)
    info = {int(gid): int(gcount) for gid, gcount in info.items()}

    # 后端处理需求
    # 获取商品id，查询库存是否满足
    # 取出金额，生成订单
    # 减库存、加销量

    uid = request.user.id

    # 订单编号按照年月日时分秒来生成,后面加上9位的用户id
    order_code = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "%09d" % uid

    # 开启事务
    with transaction.atomic():

        # 创建事务的保存点
        save_id = transaction.savepoint()

        # 先生成总订单
        orderinfo = OrderInfo.objects.create(
            uid=uid,
            order_code=order_code,
            total_count=sum(info.values()),
            total_amount=0
        )

        total_price = 0

        # 循环info字典中商品，判断库存，获取金额
        for good_id, good_count in info.items():

            while True:
                # 先获取商品id对应的商品数据
                good = Goods.objects.get(id=good_id)

                # 使用悲观锁
                # good = Goods.objects.select_for_update().get(id=good_id)

                # 判断库存不够
                if good.stock < good_count:
                    # 回滚事务
                    transaction.savepoint_rollback(save_id)
                    return render_json(error.STOCK_NOT_FILLED, '商品库存不足')

                # 模拟并发操作
                import time
                time.sleep(5)

                # 减库存加销量
                # good.stock = good.stock - good_count
                # good.sales = good.sales + good_count
                # good.save()

                # 使用乐观锁操作
                stock_new = good.stock - good_count
                sales_new = good.sales + good_count

                print(uid, '----', good.id, '-----', good.stock)
                res = Goods.objects.filter(id=good.id, stock=good.stock).update(
                    stock=stock_new,
                    sales=sales_new,
                )

                if res == 0:
                    continue
                    # # 回滚事务
                    # transaction.savepoint_rollback(save_id)
                    # return render_json(data='服务器忙，请稍后操作')

                # 取出商品总金额
                total_price += good.price * good_count

                # 生成子订单
                OrderDetail.objects.create(
                    uid=uid,
                    order_code=order_code,
                    goods_id=good.id,
                    counts=good_count,
                    price=good.price
                )

                break

        # 保存总订单的总金额
        orderinfo.total_amount = total_price
        orderinfo.save()

        # 提交事务
        transaction.savepoint_commit(save_id)

    return render_json(data='订单生成成功')





# 支付接口
def pay(request):
    alipay = AliPay(
        appid='2016092700609211',
        app_notify_url=None,  # 默认回调url
        app_private_key_path=os.path.join(settings.BASE_DIR, "alipay/app_private_key.pem"),
        alipay_public_key_path=os.path.join(settings.BASE_DIR, "alipay/alipay_public_key.pem"),
        sign_type="RSA2",
        debug=True
    )

    # 生成登录支付宝连接
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no='20190902064432000000013',
        total_amount='2000',
        subject='礼物支付',
        return_url='http://127.0.0.1:8000/orders/alipayback/',
    )

    alipay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
    return redirect(alipay_url)



def alipayback(request):
    query_dict = request.GET
    data = query_dict.dict()

    print(data)
    # 获取并从请求参数中剔除signature
    signature = data.pop('sign')

    # 创建支付宝支付对象
    alipay = AliPay(
        appid='2016092700609211',
        app_notify_url=None,  # 默认回调url
        app_private_key_path=os.path.join(settings.BASE_DIR, "alipay/app_private_key.pem"),
        alipay_public_key_path=os.path.join(settings.BASE_DIR, "alipay/alipay_public_key.pem"),
        sign_type="RSA2",
        debug=True
    )
    # 校验这个重定向是否是alipay重定向过来的
    success = alipay.verify(data, signature)
    if success:
        #	验证成功
        # 生成支付记录，改变订单状态
        print('yes')
        return render_json('yes')
    else:
      	# 验证失败
        print('no')
        return render_json('no')