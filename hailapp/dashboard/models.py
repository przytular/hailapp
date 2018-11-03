# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from decimal import Decimal
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

COUNTRIES = (
    ('canada', 'Canada'),
)

CLAIM_STATES = (
    ('started', 'started'),
    ('assigned', 'assigned'),
    ('completed', 'completed')
)

FIELD_TYPES = (
    ('cereals', 'Cereals'),
    ('oilseeds', 'Oilseeds'),
    ('pulses', 'Pulses'),
)

class Adjuster(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    photo = models.ImageField(upload_to='adjusters', blank=True,
                        default='person-placeholder.png')
    lat = models.CharField(max_length=20, blank=True)
    lng = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)



class Claim(models.Model):
    # Meta
    created = models.DateTimeField(auto_now_add=True)
    adjusters = models.ManyToManyField(Adjuster, blank=True)

    # Client information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    addr_street_1 = models.CharField(max_length=50)
    addr_street_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)

    # Loss information
    policy_no = models.CharField(max_length=50)
    loss_no = models.CharField(max_length=50, blank=True)
    date_of_loss = models.DateField(null=True, blank=True)
    state = models.CharField(max_length=100, default='started', choices=CLAIM_STATES)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    time_limit = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ['created']

    @property
    def assigned(self):
        return ", ".join([adj.full_name for adj in self.adjusters.all()])

    @property
    def time_left(self):
        if self.time_limit:
            return datetime.strftime(self.time_limit, "%Y-%m-%d %H:%M")
        else:
            return "No limit"


class ClaimField(models.Model):
    claim = models.ForeignKey(Claim)
    type = models.CharField(max_length=50, choices=FIELD_TYPES)
    name = models.CharField(max_length=50, blank=True)
    acres = models.IntegerField()
    quarter = models.CharField(max_length=20, blank=True)
    section = models.CharField(max_length=20, blank=True)
    township = models.CharField(max_length=20, blank=True)
    range = models.CharField(max_length=20, blank=True)
    meridian = models.CharField(max_length=20, blank=True)
    loss = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)
    completed = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='fields', blank=True, null=True)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_delete, sender=Adjuster)
def ensure_profile_exists(sender, instance, **kwargs):
    user = instance.user
    user.is_active = False
    user.save()
