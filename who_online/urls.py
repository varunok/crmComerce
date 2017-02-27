# -*- coding: utf-8 -*-


from django.conf.urls import url
from who_online.views import who_online, who_online_html

urlpatterns = [
    url(r'who_online$', who_online, name='who_online'),
    url(r'who_online_html$', who_online_html, name='who_online_html'),
]
