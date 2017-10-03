# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Adjuster, Claim


@method_decorator(login_required, name='dispatch')
class MapView(TemplateView):
    template_name = 'dashboard/map.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MapView, self).get_context_data(*args, **kwargs)
        context['adjusters'] = Adjuster.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class SendClaimView(CreateView):
    model = Claim
    fields = '__all__'
    success_url = reverse_lazy('map')


@method_decorator(login_required, name='dispatch')
class OpenClaimsView(TemplateView):
    template_name = 'dashboard/open_claims.html'
    def get_context_data(self, *args, **kwargs):
        context = super(OpenClaimsView, self).get_context_data(*args, **kwargs)
        context['claims'] = Claim.objects.filter(completed=False)
        context['adjusters'] = Adjuster.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class CompletedClaimsView(TemplateView):
    template_name = 'dashboard/completed_claims.html'
    def get_context_data(self, *args, **kwargs):
        context = super(CompletedClaimsView, self).get_context_data(*args, **kwargs)
        context['claims'] = Claim.objects.filter(completed=True)
        return context


@method_decorator(login_required, name='dispatch')
class AdjustersView(TemplateView):
    template_name = 'dashboard/adjusters.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AdjustersView, self).get_context_data(*args, **kwargs)
        context['adjusters'] = Adjuster.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class CreateAdjusterView(CreateView):
    model = Adjuster
    fields = ['first_name', 'last_name', 'phone', 'email', 'photo']
    success_url = reverse_lazy('adjusters')


@method_decorator(login_required, name='dispatch')
class AdjusterProfileView(DetailView):
    model = Adjuster


@method_decorator(login_required, name='dispatch')
class AdjusterProfileUpdateView(UpdateView):
    model = Adjuster
    fields = ['first_name', 'last_name', 'phone', 'email', 'photo']
    success_url = reverse_lazy('adjusters')


@method_decorator(login_required, name='dispatch')
class UpdateClaimsView(UpdateView):
    model = Claim
    fields = '__all__'
    success_url = reverse_lazy('open_claims')