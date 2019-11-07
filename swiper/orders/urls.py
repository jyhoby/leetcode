from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^commits/$', api.commits),
    url(r'^pay/$', api.pay),
    url(r'^alipayback/$', api.alipayback)
]