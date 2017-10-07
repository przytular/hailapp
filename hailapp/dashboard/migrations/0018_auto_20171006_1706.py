# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20171006_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claimfield',
            name='land_location',
        ),
        migrations.AddField(
            model_name='claimfield',
            name='_range',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='claimfield',
            name='meridian',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='claimfield',
            name='quarter',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='claimfield',
            name='section',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='claimfield',
            name='township',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='claimfield',
            name='acres',
            field=models.CharField(max_length=20),
        ),
    ]
