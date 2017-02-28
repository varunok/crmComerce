# -*- coding: utf-8 -*-


import uuid
import os
from django.db import models
from setting_street.models import Street, District, Subway
from django.contrib.auth.models import User
# from extuser.models import MyUser
from setting_globall.models import NationalCarrency


# Create your models here.

class UserFullName(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return '%s' % self.get_full_name()


class ImagesFacility(models.Model):
    class Meta(object):
        verbose_name = u'Фото обекта'
        verbose_name_plural = u'Фото объектов'

    album = models.ForeignKey('AddressFacilityData',
                              verbose_name=u'Альбом',
                              on_delete=models.CASCADE,
                              related_name='photos')

    image = models.ImageField(verbose_name=u'Фото', upload_to='img_obj/%Y/%m/%d/%H/%M/')

    cover = models.BooleanField(verbose_name=u'Обложка', default=0)

    def __unicode__(self):
        return '%s' % self.album


class TypeFacility(models.Model):
    class Meta(object):
        verbose_name = u'Тип обекта'
        verbose_name_plural = u'Типы объектов'

    type_facility = models.CharField(max_length=50,
                                     unique=True,
                                     verbose_name=u'Тип обекта')

    def __unicode__(self):
        return '%s' % self.type_facility


class TypeOperations(models.Model):
    class Meta(object):
        verbose_name = u'Тип операции'
        verbose_name_plural = u'Типы операций'

    type_operations = models.CharField(max_length=50,
                                       unique=True,
                                       blank=True,
                                       null=True,
                                       verbose_name=u'Тип операции')

    def __unicode__(self):
        return '%s' % self.type_operations


class TypeContactOwner(models.Model):
    class Meta(object):
        verbose_name = u'Тип контакта владельца'
        verbose_name_plural = u'Типы контактов владельца'

    type_contact_owner = models.CharField(max_length=50,
                                          unique=True,
                                          blank=False,
                                          null=True,
                                          verbose_name=u'Тип контакта владельца')

    def __unicode__(self):
        return '%s' % self.type_contact_owner


class TypeRepairs(models.Model):
    class Meta(object):
        verbose_name = u'Тип ремонта'
        verbose_name_plural = u'Типы ремонта'

    type_repairs = models.CharField(max_length=50,
                                    unique=True,
                                    blank=False,
                                    null=True,
                                    verbose_name=u'Тип ремонта')

    def __unicode__(self):
        return '%s' % self.type_repairs


class TypeActuality(models.Model):
    class Meta(object):
        verbose_name = u'Тип актуальности'
        verbose_name_plural = u'Типы актуальности'

    type_actuality = models.CharField(max_length=50,
                                      unique=True,
                                      blank=False,
                                      null=True,
                                      verbose_name=u'Тип актуальности')

    def __unicode__(self):
        return '%s' % self.type_actuality


class TypeCondition(models.Model):
    class Meta(object):
        verbose_name = u'Тип состояния'
        verbose_name_plural = u'Типы состояния'

    type_condition = models.CharField(max_length=50,
                                      unique=True,
                                      blank=False,
                                      null=True,
                                      verbose_name=u'Тип состояния')

    def __unicode__(self):
        return '%s' % self.type_condition


class TypeHeating(models.Model):
    class Meta(object):
        verbose_name = u'Тип Отопления'
        verbose_name_plural = u'Типы Отоплений'

    type_heating = models.CharField(max_length=50,
                                    unique=True,
                                    blank=False,
                                    null=True,
                                    verbose_name=u'Тип Отопления')

    def __unicode__(self):
        return '%s' % self.type_heating


class TypeLocations(models.Model):
    class Meta(object):
        verbose_name = u'Тип Расположения'
        verbose_name_plural = u'Типы Расположения'

    locations = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name=u'Тип Расположения')

    def __unicode__(self):
        return '%s' % self.locations


class TypeStoreys(models.Model):
    class Meta(object):
        verbose_name = u'Тип Этажности'
        verbose_name_plural = u'Типы Этажности'

    storeys = models.CharField(max_length=50,  unique=True, blank=True, null=True, verbose_name=u'Тип Этажности')

    def __unicode__(self):
        return '%s' % self.storeys


class TypeEntrance(models.Model):
    class Meta(object):
        verbose_name = u'Тип Входа'
        verbose_name_plural = u'Типы Входов'

    entrances = models.CharField(max_length=50,  unique=True, blank=True, null=True, verbose_name=u'Тип Входа')

    def __unicode__(self):
        return '%s' % self.entrances


class TypeDocumentation(models.Model):
    class Meta(object):
        verbose_name = u'Тип Документа'
        verbose_name_plural = u'Типы Документов'

    documentations = models.CharField(max_length=50,  unique=True, blank=True, null=True, verbose_name=u'Тип Документа')

    def __unicode__(self):
        return '%s' % self.documentations


class TypeUnderThat(models.Model):
    class Meta(object):
        verbose_name = u'Тип Под что'
        verbose_name_plural = u'Типы Под что'

    under_thats = models.CharField(max_length=50,  unique=True, blank=True, null=True, verbose_name=u'Тип Под что')

    def __unicode__(self):
        return '%s' % self.under_thats


class TypeAvailability(models.Model):
    class Meta(object):
        verbose_name = u'Тип Наличие'
        verbose_name_plural = u'Типы Наличие'

    availabilitys = models.CharField(max_length=50,  unique=True, blank=True, null=True, verbose_name=u'Тип Наличие')

    def __unicode__(self):
        return '%s' % self.availabilitys



class AddressFacilityData(models.Model):
    class Meta(object):
        verbose_name = u'Адресс обекта'
        verbose_name_plural = u'Адресса объектов'

    type_facilit = models.ForeignKey('TypeFacility',
                                     to_field='type_facility',
                                     verbose_name=u"Тип обекта",
                                     blank=False,
                                     null=True,
                                     on_delete=models.PROTECT)

    street_obj = models.ForeignKey(Street,
                                   to_field='full_street',
                                   verbose_name=u'Улица',
                                   blank=False,
                                   null=True,
                                   on_delete=models.PROTECT)

    district_obj = models.ForeignKey(District,
                                     to_field='district',
                                     verbose_name=u'Район',
                                     blank=True,
                                     null=True,
                                     on_delete=models.PROTECT)

    subway_obj = models.ForeignKey(Subway,
                                   to_field='subway',
                                   verbose_name=u'Метро',
                                   blank=True,
                                   null=True,
                                   on_delete=models.PROTECT)

    number_home = models.IntegerField(verbose_name=u'Номер дома',
                                      blank=True,
                                      null=True)

    literal = models.CharField(max_length=10,
                               verbose_name=u'Буквенный индекс',
                               blank=True,
                               null=True)

    number_apartment = models.CharField(max_length=10,
                                        verbose_name=u'Номер квартиры',
                                        blank=True,
                                        null=True)

    price_bay = models.IntegerField(default=0,
                                    verbose_name=u'Цена(выкуп)')

    price_month = models.IntegerField(default=0,
                                      verbose_name=u'Цена(месяц)')

    list_operations = models.ManyToManyField(TypeOperations,
                                             verbose_name=u'Тип операции',
                                             blank=False)

    landmark = models.CharField(max_length=500,
                                verbose_name=u'Ориентир',
                                blank=True,
                                null=True)


    # start Описание объекта

    location = models.ForeignKey(TypeLocations,
                                 to_field='locations',
                                 verbose_name=u'Расположение',
                                 blank=True,
                                 null=True,
                                 on_delete=models.PROTECT)

    footage = models.PositiveSmallIntegerField(verbose_name=u'Метраж', blank=True, null=True)

    shopping_room = models.PositiveSmallIntegerField(verbose_name=u'Торговый зал', blank=True, null=True)

    # поле ремонт
    repairs = models.ForeignKey(TypeRepairs,
                                to_field='type_repairs',
                                verbose_name=u'Ремонт',
                                blank=True,
                                null=True,
                                on_delete=models.PROTECT)

    number_of_storeys = models.ForeignKey(TypeStoreys,
                                to_field='storeys',
                                verbose_name=u'Этажность',
                                blank=True,
                                null=True,
                                on_delete=models.PROTECT)

    entrance = models.ForeignKey(TypeEntrance,
                                to_field='entrances',
                                verbose_name=u'Вход',
                                blank=True,
                                null=True,
                                on_delete=models.PROTECT)

    payments = models.CharField(max_length=100,
                                verbose_name=u'Платежи',
                                blank=True,
                                null=True)

    rooms = models.CharField(max_length=200,
                             verbose_name=u'Комнат',
                             blank=True,
                             null=True)

    documentation = models.ForeignKey(TypeDocumentation,
                                to_field='documentations',
                                verbose_name=u'Документы',
                                blank=True,
                                null=True,
                                on_delete=models.PROTECT)

    comment = models.TextField(verbose_name=u'Комментарий',
                               blank=False,
                               null=True)
    # end Описание объекта

    # start Состояние объекта
    rieltor = models.ManyToManyField(UserFullName,
                                     blank=True,
                                     verbose_name=u'Риелтор')

    loyality = models.ManyToManyField(UserFullName,
                                      blank=True,
                                      verbose_name=u'Лояльность',
                                      related_name='loyal')

    actuality = models.ForeignKey(TypeActuality,
                                  blank=True,
                                  null=True,
                                  on_delete=models.PROTECT,
                                  verbose_name=u'Актуальность')

    condition = models.ForeignKey(TypeCondition,
                                  blank=True,
                                  null=True,
                                  on_delete=models.PROTECT,
                                  verbose_name=u'Состояние')

    commission = models.CharField(max_length=10,
                                  verbose_name=u'Комиссия',
                                  blank=True,
                                  null=True)
    # end Состояние объекта
    # start Реклама объекта
    currency = models.ForeignKey(NationalCarrency,
                                 blank=True,
                                 null=True,
                                 on_delete=models.PROTECT,
                                 verbose_name=u'Валюта',
                                 default=2)

    images_count = models.IntegerField(verbose_name=u'Количество фото', editable=True, default=0)

    title = models.CharField(max_length=250,
                             verbose_name=u'Заголовок',
                             blank=True,
                             null=True)

    youtube = models.TextField(verbose_name=u'YouTube',
                               blank=True,
                               null=True)

    panorama = models.TextField(verbose_name=u'Панорама',
                                blank=True,
                                null=True)
    # end Реклама объекта




    # start Дополнительные параметры
    heating = models.ForeignKey(TypeHeating,
                                blank=True,
                                null=True,
                                on_delete=models.PROTECT,
                                verbose_name=u'Отопление')

    under_that = models.ManyToManyField(TypeUnderThat,
                                   blank=True,
                                   verbose_name=u'Под Что')

    availability = models.ManyToManyField(TypeAvailability,
                                   blank=True,
                                   verbose_name=u'Наличие')


    date_of_renovation = models.DateTimeField(verbose_name=u'Дата обновления', auto_now=True)

    date_added = models.DateTimeField(verbose_name=u'Дата добавления', auto_now_add=True)

    public = models.BooleanField(verbose_name=u'Публикуеться', default=0)

    def __unicode__(self):
        return '%s' % (self.id)


class ContactOwner(AddressFacilityData):
    class Meta(object):
        verbose_name = u'Контакты владельца'
        verbose_name_plural = u'Контакты владельцев'
        ordering = ['id']

    contact_owner = models.ForeignKey(TypeContactOwner,
                                      blank=True,
                                      null=True,
                                      on_delete=models.PROTECT,
                                      verbose_name=u'Тип контакта владельца')

    agency = models.CharField(max_length=250,
                              verbose_name=u'Агенство',
                              blank=True)

    name_owner = models.CharField(max_length=250,
                                  verbose_name=u'Имя владельца',
                                  blank=True)

    review_date = models.DateField(verbose_name=u'Пересмотр Дата',
                                   blank=True,
                                   null=True)

    review_time = models.TimeField(verbose_name=u'Пересмотр Время',
                                   null=True,
                                   auto_now_add=True)

    call_date = models.DateField(verbose_name=u'Звонок Дата',
                                 blank=True,
                                 null=True)

    call_time = models.TimeField(verbose_name=u'Звонок Время',
                                 null=True,
                                 auto_now_add=True)

    email_owner = models.EmailField(max_length=150,
                                    null=True,
                                    blank=True,
                                    verbose_name=u'E-mail владельца')

    vip_owner = models.BooleanField(verbose_name='Vip')

    phone_owner = models.CharField(verbose_name=u'Телефон',
                                   blank=False,
                                   null=True,
                                   max_length=16)

    phone_owner_plus = models.CharField(verbose_name=u'Допол. Телефон',
                                        blank=True,
                                        null=True,
                                        max_length=16)

    trash = models.BooleanField(verbose_name='Корзина', default=False)

    time_trash = models.DateTimeField(verbose_name='Время удаления',
                                      blank=True,
                                      null=True)

    name_user_trash = models.CharField(max_length=100,
                                       blank=True,
                                       null=True,
                                       verbose_name='Кто удалил')

    def __unicode__(self):
        return '%s' % self.id


class PhoneOwner(models.Model):
    class Meta(object):
        verbose_name = u'Телефони владельца'
        verbose_name_plural = u'Телефони владельцев'

    phone = models.ForeignKey(ContactOwner,
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s' % (self.phone.phone_owner)


class DatabasePhoneOwner(models.Model):
    class Meta(object):
        verbose_name = u'Телефони владельца'
        verbose_name_plural = u'Телефони владельцев'

    db_id_owner = models.CharField(verbose_name=u'ID',
                                   blank=True,
                                   null=True,
                                   max_length=16)

    db_phone_owner = models.CharField(verbose_name=u'Телефон',
                                      blank=True,
                                      null=True,
                                      max_length=16)

    def __unicode__(self):
        return '%s => %s' % (self.db_id_owner, self.db_phone_owner)

