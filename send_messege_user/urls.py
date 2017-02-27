# -*- coding: utf-8 -*-


from django.conf.urls import url
from send_messege_user.views import send_messege_user, get_messege, get_new_message_html, get_text_message, reading_message

urlpatterns = [
    url(r'send_messege_user$', send_messege_user, name='send_messege_user'),
    url(r'get_messege$', get_messege, name='get_messege'),
    url(r'get_new_message_html$', get_new_message_html, name='get_new_message_html'),
    url(r'get_text_message$', get_text_message, name='get_text_message'),
    url(r'reading_message$', reading_message),
]
