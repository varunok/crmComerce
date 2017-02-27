# -*- coding: utf-8 -*-


from django.db import models
from django.utils import timezone

# Create your models here.


class Notes(models.Model):
    """class Notes"""

    class Meta(object):
        verbose_name = u"Нотатка"
        verbose_name_plural = u"Нотатки"

    text = models.TextField(verbose_name=u'Tекст Нотатки')
    name = models.CharField(max_length=50,
                            blank=True,
                            verbose_name=u'Заголовок')
    date = models.DateTimeField(default=timezone.now,
                                blank=False,
                                null=True,
                                verbose_name=u'Дата створення')

    def __unicode__(self):
        return '%s' % (self.name)
