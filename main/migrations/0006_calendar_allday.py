# Generated by Django 3.1.6 on 2021-04-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210426_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='allDay',
            field=models.BooleanField(default=True),
        ),
    ]
