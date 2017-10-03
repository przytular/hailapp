# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Adjuster, Claim


class MapView(TemplateView):
    template_name = 'dashboard/map.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MapView, self).get_context_data(*args, **kwargs)
        context['adjusters'] = Adjuster.objects.all()
        return context


class SendClaimView(CreateView):
    model = Claim
    fields = '__all__'
    success_url = reverse_lazy('map')


class OpenClaimsView(TemplateView):
    template_name = 'dashboard/open_claims.html'
    def get_context_data(self, *args, **kwargs):
        context = super(OpenClaimsView, self).get_context_data(*args, **kwargs)
        context['claims'] = Claim.objects.filter(completed=False)
        context['adjusters'] = Adjuster.objects.all()
        return context


class CompletedClaimsView(TemplateView):
    template_name = 'dashboard/completed_claims.html'
    def get_context_data(self, *args, **kwargs):
        context = super(CompletedClaimsView, self).get_context_data(*args, **kwargs)
        context['claims'] = Claim.objects.filter(completed=True)
        return context


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


class AdjusterProfileView(DetailView):
    model = Adjuster


class AdjusterProfileUpdateView(UpdateView):
    model = Adjuster
    fields = ['first_name', 'last_name', 'phone', 'email', 'photo']
    success_url = reverse_lazy('adjusters')


class UpdateClaimsView(UpdateView):
    model = Claim
    fields = '__all__'
    success_url = reverse_lazy('open_claims')