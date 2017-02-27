# -*- coding: utf-8 -*-


from django.forms import ModelForm, TextInput, Select, SelectMultiple
from makler.models import Makler


class MaklerForm(ModelForm):
    class Meta:
        model = Makler
        fields = ('name', 'agency', 'cooperation', 'email', 'phone', 'phone_second', 'phone_third', 'site', 'white_black', 'rieltor')
        widgets = {
            'phone': TextInput(attrs={}),
            'email': TextInput(attrs={}),
            'site': TextInput(attrs={}),
            'white_black': Select(attrs={'style': 'min-width: 100%'}),
            'cooperation': Select(attrs={'style': 'min-width: 100%'}),
            'rieltor': Select(attrs={'style': 'min-width: 100%'}),
        }
