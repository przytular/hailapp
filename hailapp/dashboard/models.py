# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

COUNTRIES = (
    ('canada', 'Canada'),
)

class Adjuster(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    photo = models.ImageField(upload_to='adjusters', blank=True,
                        default='person-placeholder.png')
    lat = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    lng = models.DecimalField(max_digits=12, decimal_places=8, null=True)

    def __unicode__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        u = User.objects.create(username=instance.email)
        self.user = u
        super(Adjuster, self).save(*args, **kwargs)


class Claim(models.Model):
    # Meta
    created = models.DateTimeField(auto_now_add=True)
    assigned = models.ForeignKey(Adjuster, null=True, blank=True)

    # Client information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    addr_street_1 = models.CharField(max_length=50)
    addr_street_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    phone = models.CharField(max_length=50)

    # Loss information
    policy_no = models.CharField(max_length=50)
    loss_no = models.CharField(max_length=50, blank=True)
    date_of_loss = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

class DamagedFields(models.Model):
    claim = models.ForeignKey(Claim)
    land_location = models.CharField(max_length=255)
    crop_type = models.CharField(max_length=50)
    acres = models.CharField(max_length=10)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)