# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-02 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20171002_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='date_of_loss',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]