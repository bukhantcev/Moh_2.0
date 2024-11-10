from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Username')
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    podrazdelenie = models.CharField(max_length=50, verbose_name='Название подразделения', default='', blank=True)
    dolgnost = models.CharField(max_length=50, verbose_name='Должность', default='', blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'