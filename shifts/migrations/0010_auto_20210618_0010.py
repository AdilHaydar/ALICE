# Generated by Django 3.1.6 on 2021-06-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0009_auto_20210617_2332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academictitle',
            options={},
        ),
        migrations.AddField(
            model_name='academictitle',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='academictitle',
            name='lft',
            field=models.PositiveIntegerField(default=2, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='academictitle',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='academictitle',
            name='rght',
            field=models.PositiveIntegerField(default=3, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='academictitle',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=4, editable=False),
            preserve_default=False,
        ),
    ]
