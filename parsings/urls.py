# -*- coding: utf-8 -*-


from django.conf.urls import url
from parsings.views import services, parser_olx, parse, setting_olx, sity_conf, site_url, ajax_phone, \
    selector_getlink_categories, selector_gettext_categories, selector_getlink_articles, selector_sity, \
    selector_title, selector_date, parser_hi_dn_ua, parsehidnua

urlpatterns = [
    url(r'services$', services, name='services'),
    url(r'parser_olx$', parser_olx, name='parser_olx'),
    url(r'parser_hi_dn_ua$', parser_hi_dn_ua, name='parser_hi_dn_ua'),
    url(r'parse$', parse),
    url(r'parsehidnua$', parsehidnua),
    url(r'setting_olx$', setting_olx, name='setting_olx'),
    url(r'sity_conf$', sity_conf),
    url(r'site_url$', site_url),
    url(r'ajax_phone$', ajax_phone),
    url(r'selector_getlink_categories$', selector_getlink_categories),
    url(r'selector_gettext_categories$', selector_gettext_categories),
    url(r'selector_getlink_articles$', selector_getlink_articles),
    url(r'selector_sity$', selector_sity),
    url(r'selector_title$', selector_title),
    url(r'selector_date$', selector_date),
]
