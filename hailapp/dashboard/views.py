# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import Adjuster


class MapView(TemplateView):
    template_name = 'dashboard/map.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MapView, self).get_context_data(*args, **kwargs)
        context['adjusters'] = Adjuster.objects.all()
        return context


class SendClaimView(TemplateView):
    template_name = 'dashboard/send_claim.html'


class OpenClaimsView(TemplateView):
    template_name = 'dashboard/open_claims.html'


class CompletedClaimsView(TemplateView):
    template_name = 'dashboard/completed_claims.html'


class AdjustersView(TemplateView):
    template_name = 'dashboard/adjusters.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AdjustersView, self).get_context_data(*args, **kwargs)
        context['adjusters'] = Adjuster.objects.all()
        return context

class CreateAdjusterView(CreateView):
    model = Adjuster
    fields = ['first_name', 'last_name', 'phone', 'email', 'photo']
    success_url = reverse_lazy('adjusters')
