# Generated by Django 4.2.16 on 2024-11-03 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0030_alter_event_date_alter_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 3, 12, 33, 26, 139444), verbose_name='Дата мероприятия'),
        ),
    ]
