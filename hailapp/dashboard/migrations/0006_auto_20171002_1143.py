# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20170930_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjuster',
            name='photo',
            field=models.ImageField(blank=True, default='person-placeholder.png', upload_to='adjusters'),
        ),
    ]