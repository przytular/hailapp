# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0027_claimfield_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adjuster',
            name='push_id',
        ),
        migrations.AlterField(
            model_name='claim',
            name='date_of_loss',
            field=models.DateField(blank=True, null=True),
        ),
    ]
