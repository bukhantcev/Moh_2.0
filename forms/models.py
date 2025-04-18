from django.db import models
from colorfield.fields import ColorField
from datetime import datetime
from django.utils import timezone
from accounts.models import Profile

class Event_type(models.Model):

    type = models.CharField('Тип мероприятия', max_length=150)
    button_color = ColorField(default='#000', verbose_name='Цвет кнопки')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип события'
        verbose_name_plural = 'Типы событий'

class Event_location(models.Model):
    location = models.CharField('Место проведения', max_length=150, default='')
    city = models.CharField('Город', max_length=150, default='', blank=True)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Место проведения события'
        verbose_name_plural = 'Места проведения событий'

class Event_name(models.Model):
    name = models.CharField('Название', max_length=150, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название события'
        verbose_name_plural = 'Названия событий'

class Event(models.Model):
    class Staff(models.TextChoices):
        ANSWER_YES = 'Да', 'Да'
        ANSWER_NO = 'Нет', 'Нет'

    date = models.DateTimeField('Дата мероприятия', default=timezone.now)
    type = models.ForeignKey(Event_type, on_delete=models.CASCADE, verbose_name='Тип мероприятия', blank=True, null=True)
    name = models.ForeignKey(Event_name, on_delete=models.CASCADE, verbose_name='Название мероприятия', blank=True, null=True)
    location = models.ForeignKey(Event_location, on_delete=models.CASCADE, verbose_name='Место проведения мероприятия', blank=True, null=True)
    svet = models.CharField(choices=Staff.choices,verbose_name='Свет', max_length=150, default=Staff.ANSWER_YES)
    zvuk = models.CharField(choices=Staff.choices,verbose_name='Звук', max_length=150, default=Staff.ANSWER_YES)
    video = models.CharField(choices=Staff.choices,verbose_name='Видео', max_length=150, default=Staff.ANSWER_YES)
    decor = models.CharField(choices=Staff.choices,verbose_name='Декорация', max_length=150, default=Staff.ANSWER_YES)
    rekvizit = models.CharField(choices=Staff.choices,verbose_name='Реквизит', max_length=150, default=Staff.ANSWER_YES)
    grim = models.CharField(choices=Staff.choices,verbose_name='Грим', max_length=150, default=Staff.ANSWER_YES)
    kostum = models.CharField(choices=Staff.choices,verbose_name='Костюм', max_length=150, default=Staff.ANSWER_YES)
    utochneniya = models.TextField(verbose_name='Уточнения', max_length=150, blank=True)
    staff = models.ManyToManyField(Profile, verbose_name='Назначенные сотрудники', blank=True)

    def __str__(self):
        return f'{self.date:%B %d, %Y} {self.type} "{self.name}"  Время: {str(self.date).split(" ")[1].split(":")[0]}:{str(self.date).split(" ")[1].split(":")[1]}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'