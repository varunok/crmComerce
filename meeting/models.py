# -*- coding: utf-8 -*-


from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from facility.models import ContactOwner
from arendator.models import Arendator
from buyer.models import Buyer


# Create your models here.

class UserFullName(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.get_full_name()


class TypeStatus(models.Model):
    class Meta:
        verbose_name = u'Тип статуса'
        verbose_name_plural = u'Типи статусов'

    status = models.CharField(max_length=100, verbose_name=u'Тип статуса', blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.status


class Meeting(models.Model):
    class Meta:
        verbose_name = u'Встречи'
        verbose_name_plural = u'Встречи'
        ordering = ['meet_date']

    meet_date = models.DateTimeField(verbose_name=u'Дата')
    # meet_date = models.DateTimeField(verbose_name=u'Дата', default=datetime.now().strftime('%d-%m-%Y %H:%M'))

    rieltor = models.ForeignKey(UserFullName,
                                blank=True,
                                verbose_name=u'Риелтор',
                                null=True,
                                on_delete=models.PROTECT)

    access = models.ManyToManyField(UserFullName,
                                    blank=True,
                                    verbose_name=u'Доступ',
                                    related_name='access')

    meet_status = models.ForeignKey(TypeStatus,
                                    verbose_name=u'Статус',
                                    blank=True,
                                    null=True,
                                    on_delete=models.PROTECT)

    meet_comment = models.TextField(verbose_name=u'Коментарий', blank=True, null=True)

    meet_facility = models.ForeignKey(ContactOwner,
                                      verbose_name=u'ID(O) Объект',
                                      blank=True,
                                      null=True,
                                      on_delete=models.CASCADE)

    meet_arendator = models.ForeignKey(Arendator,
                                       verbose_name=u'ID(A) Арендатор',
                                       blank=True,
                                       null=True,
                                       on_delete=models.CASCADE)

    meet_buyer = models.ForeignKey(Buyer,
                                   verbose_name=u'ID(P) Покупатель',
                                   blank=True,
                                   null=True,
                                   on_delete=models.CASCADE)

    meet_trash = models.BooleanField(verbose_name='В корзину', default=False)

    meet_archiv = models.BooleanField(verbose_name='В архив', default=False)

    add_date = models.DateTimeField(verbose_name=u'Дата добавления', auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.id
