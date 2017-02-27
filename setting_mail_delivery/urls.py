# -*- coding: utf-8 -*-


from django.conf.urls import url
from setting_mail_delivery.views import setting_mail_delivery, sms_template, save_sms_template_form, \
    email_template, save_email_template_form, sms_setting, save_sms_setting, save_email_setting, \
    email_setting

urlpatterns = [
    url(r'^setting_mail_delivery$', setting_mail_delivery, name='setting_mail_delivery'),
    url(r'^sms_template$', sms_template, name='sms_template'),
    url(r'^email_template$', email_template, name='email_template'),
    url(r'^save_sms_template_form$', save_sms_template_form, name='save_sms_template_form'),
    url(r'^save_email_template_form$', save_email_template_form, name='save_email_template_form'),
    url(r'^sms_setting$', sms_setting, name='sms_setting'),
    url(r'^email_setting$', email_setting, name='email_setting'),
    url(r'^save_sms_setting$', save_sms_setting, name='save_sms_setting'),
    url(r'^save_email_setting', save_email_setting, name='save_email_setting'),
]
