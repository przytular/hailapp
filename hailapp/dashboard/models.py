# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

COUNTRIES = (
    (0, 'Canada'),
)

class Adjuster(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to='adjusters', blank=True,
                        default='person-placeholder.png')
    lat = models.CharField(max_length=20, blank=True)
    lng = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Claim(models.Model):
    # Meta
    created = models.DateTimeField(auto_now_add=True)
    assigned = models.ForeignKey(Adjuster, blank=True)

    # Client information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    addr_street_1 = models.CharField(max_length=50)
    addr_street_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    phone = models.CharField(max_length=50)

    # Loss information
    policy_no = models.CharField(max_length=50)
    loss_no = models.CharField(max_length=50, blank=True)
    date_of_loss = models.DateTimeField(blank=True)


class DamagedFields(models.Model):
    claim = models.ForeignKey(Claim)
    land_location = models.CharField(max_length=255)
    crop_type = models.CharField(max_length=50)
    acres = models.CharField(max_length=10)
