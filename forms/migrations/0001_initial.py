# Generated by Django 5.1 on 2024-08-31 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата мероприятия')),
                ('type', models.CharField(max_length=150, verbose_name='Тип мероприятия')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('location', models.CharField(max_length=150, verbose_name='Место проведения')),
                ('staff', models.CharField(max_length=150, verbose_name='Службы')),
            ],
        ),
    ]