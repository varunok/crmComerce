# -*- coding: utf-8 -*-


from django import template


register = template.Library()


@register.filter(name='get_value')
def get_value(dictionary, key):
    try:
        return dictionary.get(key)
    except:
        return ""
