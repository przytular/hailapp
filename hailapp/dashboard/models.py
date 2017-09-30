# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Adjuster(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
