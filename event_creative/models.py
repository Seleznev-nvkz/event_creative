# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from PIL import Image
from os.path import isfile


def img_resize(obj):
    if obj.image:
        img_path = obj.image._get_path()
        if isfile(img_path):
            image = Image.open(img_path)
            if image.size > 800:
                percent = 800.0/image.size[0]
                image.thumbnail((800, int(image.size[1]*percent)), Image.ANTIALIAS)
                image.save(img_path, quality=90)


class ImageTable(models.Model):
    image = models.ImageField()

    def __unicode__(self):
        return self.image.url


class Article(models.Model):
    """
    Статья
    """
    title = models.CharField(max_length=128,  verbose_name=u'Заголовок')
    body = RedactorField(verbose_name=u'Текст статьи')
    create_date = models.DateTimeField(verbose_name=u'Дата создания')
    active = models.BooleanField(default=True, verbose_name=u'Показывать')
    image = models.ImageField(verbose_name=u'Постер', blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name=u'Дата изменения')

    class Meta:
        verbose_name = verbose_name_plural = u'Статьи'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', args=[str(self.pk), ])


class Report(models.Model):
    """
    Отчет
    """
    main_title = models.CharField(max_length=32,  verbose_name=u'Основной Заголовок')
    add_title = models.CharField(max_length=128,  verbose_name=u'Подробный заголовок')
    body = RedactorField(verbose_name=u'Текст статьи')
    create_date = models.DateTimeField(verbose_name=u'Дата создания')
    active = models.BooleanField(default=True, verbose_name=u'Показывать')
    image = models.ImageField(verbose_name=u'Постер', blank=True, null=True)
    main_show = models.BooleanField(default=False, verbose_name=u'Отображать на главной')
    update_date = models.DateTimeField(auto_now=True, verbose_name=u'Дата изменения')
    slider = models.ManyToManyField(ImageTable, null=True, blank=True, related_name='report_slider')

    class Meta:
        verbose_name = verbose_name_plural = u'Отчеты'

    def __unicode__(self):
        return self.main_title

    def get_absolute_url(self):
        return reverse('report', args=[str(self.pk), ])


class Services(models.Model):
    """
    Услуги
    """
    main_title = models.CharField(max_length=32,  verbose_name=u'Основной Заголовок')
    add_title = models.CharField(max_length=128,  verbose_name=u'Подробный заголовок')
    body = RedactorField(verbose_name=u'Текст статьи')
    create_date = models.DateTimeField(verbose_name=u'Дата создания')
    active = models.BooleanField(default=True, verbose_name=u'Показывать')
    image = models.ImageField(verbose_name=u'Постер', blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, verbose_name=u'Дата изменения')
    slider = models.ManyToManyField(ImageTable, null=True, blank=True, related_name='services_slider')

    class Meta:
        verbose_name = verbose_name_plural = u'Услуги'

    def __unicode__(self):
        return self.main_title

    def get_absolute_url(self):
        return reverse('service', args=[str(self.pk), ])


@receiver([post_save, post_delete])
def recache(**kwargs):
    if kwargs.get('instance') and isinstance(kwargs.get('instance'), (Article, Report, Services, ImageTable)):
        cache.clear()
        img_resize(kwargs.get('instance'))