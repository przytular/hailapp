# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170930_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('addr_street_1', models.CharField(max_length=50)),
                ('addr_street_2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('country', models.CharField(choices=[(0, 'Canada')], max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('policy_no', models.CharField(max_length=50)),
                ('loss_no', models.CharField(blank=True, max_length=50)),
                ('date_of_loss', models.DateTimeField(blank=True)),
                ('assigned', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Adjuster')),
            ],
        ),
        migrations.CreateModel(
            name='DamagedFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_location', models.CharField(max_length=255)),
                ('crop_type', models.CharField(max_length=50)),
                ('acres', models.CharField(max_length=10)),
                ('claim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Claim')),
            ],
        ),
    ]