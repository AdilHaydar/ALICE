# Generated by Django 3.1.6 on 2021-05-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210501_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='allDay',
        ),
        migrations.AlterField(
            model_name='calendar',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
