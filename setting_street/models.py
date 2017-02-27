# -*- coding: utf-8 -*-


from django.db import models


# Create your models here.
class TypesStreet(models.Model):
    """docstring for TypesStreet"""
    class Meta(object):
        verbose_name = u"Тип улицы"
        verbose_name_plural = u"Типы улиц"

    type_street = models.CharField(max_length=30,
                                   verbose_name=u'Тип улицы')

    short_name = models.CharField(max_length=30,
                                  verbose_name=u'Короткое название')

    def __unicode__(self):
        return '%s' % (self.short_name)


class Street(models.Model):
    """docstring for Street"""
    class Meta(object):
        verbose_name = u"Улица"
        verbose_name_plural = u"Улицы"

    street = models.CharField(max_length=50,
                              verbose_name=u'Улица')

    full_street = models.CharField(max_length=80,
                                   unique=True,
                                   null=True,
                                   verbose_name=u'Улица(полн.)')

    type_street_group = models.ForeignKey('TypesStreet',
                                          verbose_name=u"Тип улицы",
                                          blank=False,
                                          null=True,
                                          on_delete=models.PROTECT)

    def __unicode__(self):
        return '%s' % self.full_street


class District(models.Model):
    class Meta(object):
        verbose_name = u"Район"
        verbose_name_plural = u"Районы"

    district = models.CharField(max_length=50,
                                unique=True,
                                verbose_name=u"Район")

    def __unicode__(self):
        return '%s' % (self.district)


class Subway(models.Model):
    class Meta(object):
        verbose_name = u"Метро"
        verbose_name_plural = u"Метро"

    subway = models.CharField(max_length=50,
                                unique=True,
                                verbose_name=u"Метро")

    def __unicode__(self):
        return '%s' % (self.subway)