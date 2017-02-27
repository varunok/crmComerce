# -*- coding: utf-8 -*-


from django.db import models
from facility.models import ContactOwner
from arendator.models import Arendator
from buyer.models import Buyer
# Create your models here.


class TypeShows(models.Model):
    class Meta(object):
        verbose_name = u'Тип показа'
        verbose_name_plural = u'Типы Показов'

    type_shows = models.CharField(max_length=50,
                                  unique=True,
                                  blank=False,
                                  null=True,
                                  verbose_name=u'Тип показа')

    def __unicode__(self):
        return self.type_shows


class SingleObjComments(models.Model):
    class Meta(object):
        verbose_name = u'Коментарий обекта'
        verbose_name_plural = u'Коментарии объектов'

    obj_comments = models.ForeignKey(ContactOwner,
                                     verbose_name=u'Обьект',
                                     on_delete=models.CASCADE)

    comment = models.TextField(verbose_name='Коментарий')

    date_comment = models.DateTimeField(auto_now_add=True,
                                        verbose_name=u'Дата коментария')

    author_comment = models.CharField(verbose_name=u'Автор коментария',
                                      max_length=100)

    image = models.CharField(max_length=100,
                             default='0')

    type_tabs = models.CharField(max_length=20, verbose_name=u'Какая вкладка?')

    def __unicode__(self):
        return self.comment


class ShowsArendator(models.Model):
    class Meta(object):
        verbose_name = u'Показ арендаторам'
        verbose_name_plural = u'Покази арендаторам'

    type_shows_arendator = models.ForeignKey(TypeShows, verbose_name=u"Покази Арендаторам",
                                             null=True)

    array_arendator = models.ForeignKey(Arendator, null=True)

    array_cont_ower = models.ForeignKey(ContactOwner, null=True)

    def __unicode__(self):
        return '%s' % self.id


class Tie(models.Model):
    class Meta(object):
        verbose_name = u'Связка с арендатором'
        verbose_name_plural = u'Связки'

    tie_cont_owner = models.OneToOneField(ContactOwner, verbose_name=u'Обект')

    tie_arenda = models.ManyToManyField(Arendator, blank=True, verbose_name=u"Связка обекта с арендатором")

    def __unicode__(self):
        return '%s' % self.id


class ShowsBuyer(models.Model):
    class Meta(object):
        verbose_name = u'Показ покупателю'
        verbose_name_plural = u'Покази покупателям'

    type_shows_buyer = models.ForeignKey(TypeShows, verbose_name=u"Покази Покупателю", null=True)

    array_buyer = models.ForeignKey(Buyer, null=True)

    array_cont_ower = models.ForeignKey(ContactOwner, null=True)

    def __unicode__(self):
        return '%s' % self.id


class TieBuyer(models.Model):
    class Meta(object):
        verbose_name = u'Связка с покупателем'
        verbose_name_plural = u'Связки'

    tie_cont_owner = models.OneToOneField(ContactOwner, verbose_name=u'Обект')

    tie_buye = models.ManyToManyField(Buyer, blank=True, verbose_name=u"Связка обекта с покупателем")

    def __unicode__(self):
        return '%s' % self.id
