# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-03 17:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_claim_completed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='claim',
            options={'ordering': ['created']},
        ),
    ]