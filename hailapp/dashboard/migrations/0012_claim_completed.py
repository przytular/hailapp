# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-03 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20171002_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
