# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20171003_1827'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DamagedFields',
            new_name='ClaimField',
        ),
    ]