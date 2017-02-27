# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserFullName(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.get_full_name()


class TypeCooperations(models.Model):
    class Meta(object):
        verbose_name = u'Тип сотрудничества'
        verbose_name_plural = u'Типи сотрудничества'

    type_cooperation = models.CharField(max_length=50, verbose_name=u'Тип сотрудничества')

    def __unicode__(self):
        return '%s' % self.type_cooperation


class TypeWhiteBlack(models.Model):
    class Meta(object):
        verbose_name = u'Тип маклера'
        verbose_name_plural = u'Типи маклеров'

    type_white_black = models.CharField(max_length=50, verbose_name=u'Тип маклера')

    def __unicode__(self):
        return '%s' % self.type_white_black


class Makler(models.Model):
    class Meta(object):
        verbose_name = u'Маклер'
        verbose_name_plural = u'Маклера'

    name = models.CharField(max_length=30, verbose_name=u'Имя', blank=True, null=True)

    agency = models.CharField(max_length=30, verbose_name=u'Агенство', blank=True, null=True)

    white_black = models.ForeignKey(TypeWhiteBlack,
                                    verbose_name=u'Тип маклера',
                                    blank=False,
                                    null=False,
                                    on_delete=models.PROTECT)

    phone = models.CharField(max_length=15, verbose_name=u'Телефон', blank=False, null=True)

    phone_second = models.CharField(max_length=15, verbose_name=u'Телефон 2', blank=True, null=True)

    phone_third = models.CharField(max_length=15, verbose_name=u'Телефон 3', blank=True, null=True)

    site = models.URLField(verbose_name=u'Сайт', null=True, blank=True)

    email = models.EmailField(verbose_name=u'Email', null=True, blank=True)

    cooperation = models.ForeignKey(TypeCooperations,
                                    verbose_name=u'Тип сотрудничества',
                                    blank=True,
                                    null=True,
                                    on_delete=models.PROTECT)

    rieltor = models.ForeignKey(UserFullName,
                                blank=True,
                                null=True,
                                verbose_name=u'Риелтор',
                                on_delete=models.PROTECT)

    add_date = models.DateTimeField(verbose_name=u'Дата добавления', auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.id
