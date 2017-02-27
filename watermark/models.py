# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.


class Watermark(models.Model):
    class Meta:
        verbose_name = u'Водяной знак'
        verbose_name_plural = u'Водяной знак'

    text = models.CharField(verbose_name=u'Водяной знак', max_length=50, blank=True, null=True)

    watermark_img = models.ImageField(verbose_name=u'Водяной знак', upload_to='watermark')

    on_off = models.BooleanField(default=True)

    def __unicode__(self):
        return self.text