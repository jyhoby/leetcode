from django.utils.deprecation import MiddlewareMixin

from common.func import render_json
from common import error
from user.models import User


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 指定白名单
        white_name = ['/user/login/', '/user/sms/', '/orders/pay/', '/orders/alipayback/']

        url = request.path

        # 如果在白名单，直接return，返回None，就会执行view视图
        if url in white_name:
            return

        id = request.session.get('id')
        if not id:

            return render_json(error.USER_NOT_LOGIN, '用户未登陆')

        # 如果用户登录，就把用户的信息绑定到request.user属性中
        request.user = User.objects.get(id=id)