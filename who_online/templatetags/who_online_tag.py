# -*- coding: utf-8 -*-


from django import template
from django.utils import timezone

register = template.Library()


@register.filter(name='last_login')
def last_login(date_arg):
    last_login = str(timezone.now()-date_arg).split('.')[0]
    last_login = last_login.split(',')[0]
    if ':' in last_login:
        last_login = last_login.split(':')
        if int(last_login[0]) == 0 and int(last_login[1]) > 15:
            return u'был в сети %s мин назад' % last_login[1]
        elif int(last_login[0]) == 0 and int(last_login[1]) <= 15:
            return u'online'
        elif int(last_login[0]) == 1 or int(last_login[0]) == 21:
            return u'был в сети %s час %s мин назад' % (last_login[0], last_login[1])
        elif 1 < int(last_login[0]) < 5 or 21 < int(last_login[0]) < 25:
            return u'был в сети %s часа %s мин назад' % (last_login[0], last_login[1])
        elif 5 <= int(last_login[0]) <= 20:
            return u'был в сети %s часов %s мин назад' % (last_login[0], last_login[1])
    else:
        last_login = last_login.split(' ')
        if int(last_login[0]) in [1, 21, 31]:
            return u'был в сети %s день назад' % last_login[0]
        elif int(last_login[0]) in [2, 3, 4, 22, 23, 24]:
            return u'был в сети %s дня назад' % last_login[0]
        elif int(last_login[0]) > 31:
            return u'был в сети больше 1 месяца назад'
        else:
            return u'был в сети %s дней назад' % last_login[0]
    return last_login
