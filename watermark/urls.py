# -*- coding: utf-8 -*-


from django.conf.urls import url
from watermark.views import setting_watermark, create_watermark, on_off_watermark


urlpatterns = [
    url(r'^setting_watermark/$', setting_watermark, name='setting_watermark'),
    url(r'^setting_watermark/create_watermark$', create_watermark, name='create_watermark'),
    url(r'^setting_watermark/on_off_watermark$', on_off_watermark, name='on_off_watermark'),
]
