# -*- coding: utf-8 -*-


import datetime
from django import template
from django.utils import timezone
import datetime

register = template.Library()


@register.filter(name='dead_line')
def dead_line(date_arg):
    if date_arg:
        if type(date_arg) != datetime.datetime:
            date_arg = datetime.datetime.combine(date_arg, datetime.time())
        date_new = date_arg - timezone.now()
        date_new = str(date_new).split(',')
        if len(date_new) == 1:
            return True
        elif len(date_new) > 1:
            date_new = int(date_new[0].split(' ')[0])
            if date_new < 0:
                return True
        else:
            return False
    else:
        return False

@register.filter(name='new_obj')
def new_obj(date_arg):
    if date_arg:
        if type(date_arg) != datetime.datetime:
            date_arg = datetime.datetime.combine(date_arg, datetime.time())
        date_arg = date_arg + datetime.timedelta(minutes=5)
        if timezone.now() > date_arg:
            return False
        else:
            return True
    else:
        return False