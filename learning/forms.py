# -*- coding: utf-8 -*-


from django.forms import ModelForm, Textarea
from learning.models import Learn


class LearnForm(ModelForm):
    class Meta:
        model = Learn
        fields = ('title', 'youtube')
        widgets = {
            'youtube': Textarea(attrs={'rows': 5}),
        }
