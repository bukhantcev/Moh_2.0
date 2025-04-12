from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    class Status(models.TextChoices):
        NO = '0', 'Ждет подтверждения'
        YES = '1', 'Подтвержден'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Username')
    first_name = models.CharField(max_length=300, verbose_name='Имя', default='')
    last_name = models.CharField(max_length=300, verbose_name='Фамилия', default='')
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", default='')
    podrazdelenie = models.ForeignKey(to='Podrazdelenie', verbose_name='Подразделение', on_delete=models.CASCADE, null=True)
    dolgnost =  models.ForeignKey(to='Dolgnost', verbose_name='Должность', on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=Status.choices, default=Status.NO, max_length=50)
    sort_index = models.IntegerField(default=5, verbose_name='Индекс сортировки')
    is_boss = models.BooleanField(default=False, verbose_name='Начальник')
    is_bigboss = models.BooleanField(default=False, verbose_name='Завпост')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        new = Profile.objects.get(user=instance)
        new.first_name = sender.objects.get(username=instance).first_name
        new.last_name = sender.objects.get(username=instance).last_name
        new.save()


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Podrazdelenie(models.Model):
    name = models.CharField(max_length=300, verbose_name="Подразделение",)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Dolgnost(models.Model):
    name = models.CharField(max_length=300, verbose_name="Должность", )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'