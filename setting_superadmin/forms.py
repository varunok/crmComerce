# -*- coding: utf-8 -*-



from django import forms
from django.forms import ModelForm, TextInput, RadioSelect, Select, ClearableFileInput
from setting_superadmin.models import AllToCall, AllToConnect


class AllToCallForm(ModelForm):
    class Meta:
        model = AllToCall
        fields = ('phone', 'email', 'skype', 'group_vk', 'image')
        widgets = {
            'phone': TextInput(attrs={}),
            'email': TextInput(attrs={}),
            'image': ClearableFileInput(attrs={'class': 'upload_file'}),
        }


class AllToConnectForm(ModelForm):
    class Meta:
        model = AllToConnect
        fields = ('email',)
        widgets = {
            'email': TextInput(attrs={}),
        }
