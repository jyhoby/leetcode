from django.conf.urls import url
from . import api

urlpatterns = [
    url(r'^user/$', api.get_user),
    url(r'^like/$', api.like),
    url(r'^dislike/$', api.dislike),
    url(r'^superlike/$', api.superlike),
    url(r'^rewind/$', api.rewind),
    url(r'^likeme/$', api.like_me),
    url(r'^friend/$', api.friend),
]
