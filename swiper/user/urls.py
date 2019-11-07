
from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^sms/$', api.send_sms),
    url(r'^login/$', api.login),

    # 访问类视图要加上as_view()方法
    url(r'^profile/$', api.Profile.as_view()),


    url(r'^avater/$', api.avater),

]