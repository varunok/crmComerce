# -*- coding: utf-8 -*-


from django import template
from setting_globall.models import FranshiseSity

register = template.Library()


@register.simple_tag(name='sity_franshise')
def sity_franshise():
    try:
        sity = FranshiseSity.objects.get(id=1)
        return sity.sity
    except:
        return ''