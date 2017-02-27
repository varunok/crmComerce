# -*- coding: utf-8 -*-


from django.conf.urls import url
from setting_globall.views import setting_globall, nat_currency, sity_franshise, franshise, get_subscribe, \
    save_subscribe_form


urlpatterns = [
    url(r'^setting_globall$', setting_globall, name='setting_globall'),
    url(r'^nat_currency$', nat_currency),
    url(r'^sity_franshise$', sity_franshise),
    url(r'^franshise$', franshise),
    url(r'^get_subscribe$', get_subscribe, name='get_subscribe'),
    url(r'^save_subscribe_form$', save_subscribe_form, name='save_subscribe_form'),
]