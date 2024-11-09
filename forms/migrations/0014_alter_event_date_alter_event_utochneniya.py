# Generated by Django 4.2.16 on 2024-09-08 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0013_alter_event_date_alter_event_decor_alter_event_grim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 13, 48, 19, 101426), verbose_name='Дата мероприятия'),
        ),
        migrations.AlterField(
            model_name='event',
            name='utochneniya',
            field=models.TextField(max_length=150, verbose_name='Уточнения'),
        ),
    ]