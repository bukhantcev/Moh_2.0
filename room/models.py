import os
import shutil

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

class MyEvents(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название события', default='Событие')
    date = models.DateField(verbose_name='Дата', default=timezone.now().date())
    time = models.TimeField(verbose_name='Время', default=timezone.now().time())
    type = models.ForeignKey(to='Type', on_delete=models.CASCADE, verbose_name='Тип события', default='', null=True)
    desc = models.TextField(max_length=30000, verbose_name='Описание', null=True)
    file = models.FileField(verbose_name='Файлы', upload_to='user_files', null=True)
    user = models.ForeignKey(to=User, verbose_name='user', on_delete=models.CASCADE, null=True)




    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

@receiver(post_save, sender=MyEvents)
def save_file(sender, instance, **kwargs):
    try:
        os.makedirs(f'user_files/{instance.user}/{instance.id}')
    except:
        pass

    try:
        shutil.move(str(instance.file), f'user_files/{instance.user}/{instance.id}')
    except:
        pass




class Type(models.Model):
    name = models.CharField(max_length=300, verbose_name='Типы событий', default='Тип')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип события'
        verbose_name_plural = 'Типы событий'