# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UsersGroupExtUser(models.Model):

    class Meta:
        verbose_name = u"Тип пользователя"
        verbose_name_plural = u"Типи пользователей"

    type_user = models.CharField(max_length=50,
                                 blank=True,
                                 verbose_name=u'Тип пользователя')

    def __unicode__(self):
        return '%s' % (self.type_user)


class MyUser(models.Model):

    user = models.OneToOneField(User)

    image = models.ImageField(
        verbose_name='Аватарка',
        max_length=255,
        upload_to='avatar',
    )
    # type_user = models.IntegerField(verbose_name=u'Тип пользователя', null=True)

    type_user = models.ForeignKey(UsersGroupExtUser,
                                  verbose_name=u"Тип пользователя",
                                  blank=False,
                                  null=True,
                                  on_delete=models.PROTECT)

    def __unicode__(self):
        return '%s, %s' % (self.user, self.id)


class RecoveryPass(models.Model):
    """docstring for RecoveryPass"""
    class Meta:
        verbose_name = u"Восстановление пароля"
        verbose_name_plural = u"Восстановление пароля"

    email = models.CharField(max_length=100, verbose_name=u'EMAIL')

    password = models.CharField(max_length=100, verbose_name='PASS')

    def __unicode__(self):
        return '%s' % (self.email)
