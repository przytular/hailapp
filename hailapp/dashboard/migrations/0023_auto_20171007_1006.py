# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20171007_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='claimfield',
            name='loss',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='claim',
            name='state',
            field=models.CharField(choices=[('started', 'started'), ('assigned', 'assigned'), ('completed', 'completed')], default='started', max_length=100),
        ),
        migrations.AlterField(
            model_name='claimfield',
            name='acres',
            field=models.IntegerField(),
        ),
    ]
