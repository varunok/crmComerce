# -*- coding: utf-8 -*-


from django import forms
from django.forms import ModelForm, ClearableFileInput, EmailInput, PasswordInput, URLInput, TextInput
from setting_mail_delivery.models import TemplateSms, TemplateEmail, SettingSMS, SettingEmail


class TemplateSmsForm(ModelForm):
    class Meta(object):
        model = TemplateSms
        fields = ('title', 'text', 'signature')


class TemplateEmailForm(ModelForm):
    image = forms.CharField(widget=ClearableFileInput())
    image.widget.attrs['multiple'] = 'false'
    image.widget.attrs['class'] = 'upload_file'
    image.widget.attrs['accept'] = 'image/*'
    image.required = False

    class Meta(object):
        model = TemplateEmail
        fields = ('title', 'text', 'signature', 'sender_address', 'logo')
        widgets = {
            'sender_address': EmailInput(attrs={'class': 'col-md-12'}),
        }


class SettingSMSForm(ModelForm):
    class Meta:
        model = SettingSMS
        fields = ('sender', 'login', 'password',)
        widgets = {
            'password': PasswordInput(attrs={'class': 'col-md-12'}, render_value=True),
        }


class SettingEmailForm(ModelForm):
    class Meta:
        model = SettingEmail
        fields = ('host', 'host_user', 'password', 'timeout',)
        widgets = {
            'password': PasswordInput(attrs={'class': 'col-md-12'}, render_value=True),
            'host': URLInput(attrs={'class': 'col-md-12'}),
            'host_user': EmailInput(attrs={'class': 'col-md-12'}),
            'timeout': TextInput(attrs={'class': 'col-md-12'}),

        }
