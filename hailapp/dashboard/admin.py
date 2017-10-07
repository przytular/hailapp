# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Adjuster, Claim, ClaimField

admin.site.register(Adjuster)
admin.site.register(Claim)
admin.site.register(ClaimField)