# -*- coding: utf-8 -*-


from django.forms import ModelForm
from setting_globall.models import Subscribe


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ('name', 'phone')
        widgets = {
            # 'youtube': Textarea(attrs={'rows': 5}),
        }
