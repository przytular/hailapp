# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView


class MapView(TemplateView):
    template_name = 'dashboard/index.html'


class SendClaimView(TemplateView):
    template_name = 'dashboard/send_claim.html'


class OpenClaimsView(TemplateView):
    template_name = 'dashboard/open_claims.html'


class CompletedClaimsView(TemplateView):
    template_name = 'dashboard/completed_claims.html'


class AdjustersView(TemplateView):
    template_name = 'dashboard/adjusters.html'
