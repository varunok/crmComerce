# -*- coding: utf-8 -*-


from django.conf.urls import url
from posting.views import posting_true, posting_false


urlpatterns = [
    url(r'post/false$', posting_true),
    url(r'post/true$', posting_false),
]