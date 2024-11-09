# Generated by Django 4.2.16 on 2024-11-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500, verbose_name='Название спектакля')),
                ('link', models.CharField(default='', max_length=500, verbose_name='Ссылка на спектакль')),
                ('length', models.CharField(default='', max_length=50, verbose_name='Длительность спектакля')),
                ('video', models.FileField(blank=True, default='', upload_to='materials/<django.db.models.fields.CharField>/video/', verbose_name='Видео спектакля')),
                ('svet_doc', models.FileField(blank=True, default='', upload_to='materials/<django.db.models.fields.CharField>/svet_doc/', verbose_name='Свет')),
                ('zvuk_doc', models.FileField(blank=True, default='', upload_to='materials/<django.db.models.fields.CharField>/zvuk_doc/', verbose_name='Звук')),
                ('video_doc', models.FileField(blank=True, default='', upload_to='materials/<django.db.models.fields.CharField>/video_doc/', verbose_name='Видео')),
                ('decor_doc', models.FileField(blank=True, default='', upload_to='materials/<django.db.models.fields.CharField>/decor_doc/', verbose_name='Декорация')),
                ('rekv_doc', models.FileField(blank=True, default='', upload_to='materials/<django.db.models.fields.CharField>/rekv_doc/', verbose_name='Реквизит')),
                ('grim_doc', models.FileField(blank=True, default='', upload_to='materials/<django.db.models.fields.CharField>/grim_doc/', verbose_name='Грим')),
                ('kostum_doc', models.FileField(blank=True, default='', upload_to='materials/<django.db.models.fields.CharField>/kostum_doc/', verbose_name='Костюм')),
            ],
            options={
                'verbose_name': 'Спектакль',
                'verbose_name_plural': 'Спектакли',
            },
        ),
    ]