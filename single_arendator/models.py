# -*- coding: utf-8 -*-


from django.db import models
from arendator.models import Arendator


# Create your models here.


class SingleArendatorComments(models.Model):
    class Meta(object):
        verbose_name = u'Коментарий обекта'
        verbose_name_plural = u'Коментарии объектов'

    obj_comments = models.ForeignKey(Arendator,
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
