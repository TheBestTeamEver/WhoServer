# coding=utf-8
from __future__ import unicode_literals
from django.db import models


class Level(models.Model):
    name = models.CharField(u'Имя', max_length=64)
    true_photo = models.ImageField(u'Тру')
    fake_photo = models.ImageField(u'Фэйк')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Уровень'
        verbose_name_plural = u'Уровни'


class SimpleUser(models.Model):
    login = models.CharField(u'Логин', max_length=64)
    password = models.CharField(u'Пароль', max_length=64)
    rating = models.IntegerField(u'Rating', default=0)

    def __unicode__(self):
        return self.login

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
