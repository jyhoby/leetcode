from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^perm/$', api.perm),
    url(r'^rank/$', api.rank),
    url(r'^mail/$', api.mail)
]