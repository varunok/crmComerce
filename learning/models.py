# -*- coding: utf-8 -*-


from django.db import models


class Learn(models.Model):
    # TODO: Define fields here

    class Meta:
        verbose_name = u"Обучение"
        verbose_name_plural = u"Обучение"

    title = models.CharField(verbose_name=u'Заголовок', max_length=50)

    youtube = models.CharField(verbose_name=u'Видео', max_length=500)

    def __unicode__(self):
        return '%s' % self.title
