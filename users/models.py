from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Users (models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    phone_number = models.CharField('Номер телефона', max_length=11)
    tg_id = models.CharField('Телега', max_length=10)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

from django.contrib.auth.models import User

