from django.db import models

class Spect(models.Model):

    label = 'q'
    name = models.CharField(max_length=500, verbose_name="Название спектакля", unique=True)
    link = models.CharField(max_length=500, default='', verbose_name="Ссылка на спектакль", blank=True)
    length = models.CharField(max_length=50, default='', verbose_name="Длительность спектакля", blank=True)
    video = models.CharField(max_length=5000, default='', verbose_name="Видео спектакля", blank=True)
    svet_doc = models.FileField(upload_to=f'materials/{label}/svet_doc/', verbose_name='Свет', blank=True, default='')
    zvuk_doc = models.FileField(upload_to=f'materials/{label}/zvuk_doc/', verbose_name='Звук', blank=True, default='')
    video_doc = models.FileField(upload_to=f'materials/{label}/video_doc/', verbose_name='Видео', blank=True, default='')
    decor_doc = models.FileField(upload_to=f'materials/{label}/decor_doc/', verbose_name='Декорация', blank=True, default='')
    rekv_doc = models.FileField(upload_to=f'materials/{label}/rekv_doc/', verbose_name='Реквизит', blank=True, default='')
    grim_doc = models.FileField(upload_to=f'materials/{label}/grim_doc/', verbose_name='Грим', blank=True, default='')
    kostum_doc = models.FileField(upload_to=f'materials/{label}/kostum_doc/', verbose_name='Костюм', blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спектакль'
        verbose_name_plural = 'Спектакли'
