# -*- coding: utf-8 -*-


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


class TypeComplexity(models.Model):
    class Meta:
        verbose_name = u'Тип сложности'
        verbose_name_plural = u'Типи сложности'

    complexity = models.CharField(max_length=20, verbose_name=u'Тип сложности', blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.complexity


class Tasking(models.Model):
    class Meta:
        verbose_name = u'Задача'
        verbose_name_plural = u'Задачи'
        ordering = ['dead_line']

    dead_line = models.DateTimeField(verbose_name=u'Крайний срок')

    access = models.ManyToManyField(UserFullName,
                                    blank=True,
                                    verbose_name=u'Доступ',
                                    related_name='access')

    rieltor = models.ForeignKey(UserFullName,
                                blank=True,
                                verbose_name=u'Риелтор',
                                null=True,
                                on_delete=models.PROTECT)

    type_complex = models.ForeignKey(TypeComplexity,
                                     verbose_name=u'Сложность',
                                     blank=True,
                                     null=True,
                                     on_delete=models.PROTECT)

    task_facility = models.ForeignKey(ContactOwner,
                                      verbose_name=u'ID(O) Объект',
                                      blank=True,
                                      null=True,
                                      on_delete=models.CASCADE)

    task_arendator = models.ForeignKey(Arendator,
                                       verbose_name=u'ID(A) Арендатор',
                                       blank=True,
                                       null=True,
                                       on_delete=models.CASCADE)

    task_buyer = models.ForeignKey(Buyer,
                                   verbose_name=u'ID(P) Покупатель',
                                   blank=True,
                                   null=True,
                                   on_delete=models.CASCADE)

    task_text = models.TextField(verbose_name=u'Текст', blank=True, null=True)

    task_trash = models.BooleanField(verbose_name='В корзину', default=False)

    task_archiv = models.BooleanField(verbose_name='В архив', default=False)

    add_date = models.DateTimeField(verbose_name=u'Дата добавления', auto_now_add=True)
