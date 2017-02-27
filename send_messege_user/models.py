# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
from extuser.models import MyUser


class UserMessage(models.Model):
    """docstring for UserMessage"""
    class Meta(object):
        verbose_name = u'Сообщение пользователя'
        verbose_name_plural = u'Сообщения пользователей'

    user_message = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=u'Кому?')

    from_user = models.ForeignKey(MyUser,
                                  related_name='from_us',
                                  on_delete=models.PROTECT,
                                  verbose_name=u'От кого?',
                                  to_field='user')

    message = models.TextField(verbose_name=u'Сообщение')

    time_message = models.DateTimeField(verbose_name='Время отправки', auto_now_add=True)

    read = models.BooleanField(verbose_name=u'Прочитано', default=0)

    def __unicode__(self):
        return '%s...' % (self.message[0:11])
