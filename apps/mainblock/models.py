# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
import datetime
import os
from pytils.translit import translify
from apps.utils.utils import ImageField
from django.db.models.signals import post_save
from apps.utils.managers import PublishedManager
from mptt.models import MPTTModel, TreeForeignKey, TreeManager

def image_path_license(instance, filename):
    return os.path.join('images', 'licenses_imgs', translify(filename).replace(' ', '_'))


def file_path_license(instance, filename):
    return os.path.join('images', 'licenses_files', translify(filename).replace(' ', '_'))


class License(models.Model):
    title = models.CharField(max_length=120, verbose_name=u'название')
    image = ImageField(upload_to=image_path_license, verbose_name=u'изображение', )
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент',
        default=10)
    file = models.FileField(upload_to=file_path_license, verbose_name=u'файл документа', blank=True)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return u'лицензии "%s"' % self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'license')
        verbose_name_plural = _(u'licenses')

    def get_src_image(self):
        return self.image.url


def file_path_docs(instance, filename):
    return os.path.join('images', 'doc_files', translify(filename).replace(' ', '_'))


class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'название')
    file = models.FileField(upload_to=file_path_docs, verbose_name=u'файл документа')
    create_date = models.DateTimeField(verbose_name=u'дата добавления', default=datetime.datetime.now)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['-create_date']
        verbose_name = _(u'document')
        verbose_name_plural = _(u'documents')

    def get_file_path(self):
        return self.file.url


def image_path_person(instance, filename):
    return os.path.join('images', 'licenses_files', translify(filename).replace(' ', '_'))


class Person(models.Model):
    fullname = models.CharField(max_length=150, verbose_name=u'полное имя')
    post_title = models.CharField(max_length=255, verbose_name=u'должность')
    photo = ImageField(upload_to=image_path_person, verbose_name=u'фотография', blank=True)
    phone_num = models.CharField(max_length=75, verbose_name=u'телефонный номер')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент',
        default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.fullname

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'person')
        verbose_name_plural = _(u'persons')

    def get_src_photo(self):
        return self.photo.url

type_choices = (
    (u'current', u'Текущие'),
    (u'plan', u'Планируемые'),
    (u'archive', u'Архивные'),
    )

def str_price(price):
    if not price:
        return u'0'
    value = u'%s' % price
    if price._isinteger():
        value = u'%s' % value[:len(value) - 3]
        count = 3
    else:
        count = 6

    if len(value) > count:
        ends = value[len(value) - count:]
        starts = value[:len(value) - count]

        if len(starts) > 3:
            starts = u'%s %s' % (starts[:1], starts[1:len(starts)])

        return u'%s %s' % (starts, ends)
    else:
        return u'%s' % value


def file_path_PurchaseDocs(instance, filename):
    return os.path.join('images', 'purchase_files', translify(filename).replace(' ', '_'))


class Purchase(models.Model):
    title = models.CharField(max_length=120, verbose_name=u'название')
    type = models.CharField(max_length=20, verbose_name=u'статус закупки', choices=type_choices, default='plan')
    date_create = models.DateField(verbose_name=u'дата создания', default=datetime.date.today())
    price = models.DecimalField(verbose_name=u'стоимость контракта', decimal_places=2, max_digits=10)

    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'purchase')
        verbose_name_plural = _(u'purchases')

    def get_str_price(self):
        result = str_price(self.price)
        return result

    def get_documents(self):
        return self.purchaseattacheddoc_set.published()

    def get_first_document(self):
        try:
            document = self.purchaseattacheddoc_set.published()[0]
            return document
        except:
            return False


class PurchaseAttachedDoc(models.Model):
    purchase = models.ForeignKey(Purchase, verbose_name=u'закупка')
    title = models.CharField(max_length=255, verbose_name=u'название')
    protocol = models.FileField(upload_to=file_path_PurchaseDocs, verbose_name=u'файл')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент',
        default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'purchase_attached_doc')
        verbose_name_plural = _(u'purchase_attached_docs')

    def get_file_path(self):
        return self.protocol.url