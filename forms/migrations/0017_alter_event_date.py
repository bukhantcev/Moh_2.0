# Generated by Django 4.2.16 on 2024-09-08 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0016_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 8, 16, 30, 17, 106884), verbose_name='Дата мероприятия'),
        ),
    ]