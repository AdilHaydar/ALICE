# Generated by Django 3.1.6 on 2021-05-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_calendar_allday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='end',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='start',
            field=models.CharField(max_length=20),
        ),
    ]
