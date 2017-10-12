# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Adjuster, Claim, ClaimField
from django.utils.decorators import method_decorator
from .forms import NewAdjusterForm, ClaimForm, FieldForm
from django.contrib.auth import authenticate, login
from push_notifications.models import APNSDevice


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
    form_class = ClaimForm
    success_url = reverse_lazy('open_claims')

    def get_context_data(self, *args, **kwargs):
        context = super(SendClaimView, self).get_context_data(*args, **kwargs)
        context['field_form'] = FieldForm
        return context

    def form_valid(self, form):
        response = super(SendClaimView, self).form_valid(form)

        post = self.request.POST

        for i, x in enumerate(post.getlist('type')):
            if x != '':
                type = post.getlist('type')[i]
                acres = post.getlist('acres')[i]
                quarter = post.getlist('quarter')[i]
                section = post.getlist('section')[i]
                township = post.getlist('township')[i]
                range = post.getlist('range')[i]
                meridian = post.getlist('meridian')[i]

                ClaimField.objects.create(claim=self.object,
                                          type=type,
                                          acres=acres,
                                          quarter=quarter,
                                          section=section,
                                          township=township,
                                          range=range,
                                          meridian=meridian)

        try:
            user = self.object.assigned_adjuster.user
            registered_apns = APNSDevice.objects.filter(user=user)

            for apns in registered_apns:
                apns.send_message("New claim available!")
        except:
            pass

        return response


@method_decorator(login_required, name='dispatch')
class OpenClaimsView(TemplateView):
    template_name = 'dashboard/open_claims.html'
    def get_context_data(self, *args, **kwargs):
        context = super(OpenClaimsView, self).get_context_data(*args, **kwargs)
        context['claims'] = Claim.objects.filter(state__in=['assigned', 'started'])
        context['adjusters'] = Adjuster.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class CompletedClaimsView(TemplateView):
    template_name = 'dashboard/completed_claims.html'
    def get_context_data(self, *args, **kwargs):
        context = super(CompletedClaimsView, self).get_context_data(*args, **kwargs)
        context['claims'] = Claim.objects.filter(state='completed')
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
    success_url = reverse_lazy('adjusters')
    form_class = NewAdjusterForm


@method_decorator(login_required, name='dispatch')
class AdjusterProfileView(DetailView):
    model = Adjuster


@method_decorator(login_required, name='dispatch')
class AdjusterProfileUpdateView(UpdateView):
    model = Adjuster
    fields = ['first_name', 'last_name', 'phone', 'email', 'photo']
    success_url = reverse_lazy('adjusters')


@method_decorator(login_required, name='dispatch')
class UpdateClaimsView(TemplateView):
    template_name = 'dashboard/update_claims.html'

    def get_context_data(self, pk, *args, **kwargs):
        context = super(UpdateClaimsView, self).get_context_data(*args, **kwargs)
        claim = Claim.objects.get(pk=pk)
        context['form'] = ClaimForm(instance=claim)
        context['field_forms'] = []

        for f in claim.claimfield_set.all():
            context['field_forms'].append(FieldForm(instance=f))

        return context

    def post(self, request, *args, **kwargs):
        instance = Claim.objects.get(pk=kwargs['pk'])
        form = ClaimForm(request.POST, instance=instance)
        if form.is_valid():
            obj = form.save()
            post = request.POST
            fields = instance.claimfield_set.all()
            fields.delete()

            for i, x in enumerate(post.getlist('type')):
                print(x)
                type = post.getlist('type')[i]
                acres = post.getlist('acres')[i]
                quarter = post.getlist('quarter')[i]
                section = post.getlist('section')[i]
                township = post.getlist('township')[i]
                range = post.getlist('range')[i]
                meridian = post.getlist('meridian')[i]

                ClaimField.objects.create(claim=obj,
                                          type=type,
                                          acres=acres,
                                          quarter=quarter,
                                          section=section,
                                          township=township,
                                          range=range,
                                          meridian=meridian)
        if request.GET.get('completed', None):
            return HttpResponseRedirect(reverse_lazy('completed_claims'))
        else:
            return HttpResponseRedirect(reverse_lazy('open_claims'))

@method_decorator(login_required, name='dispatch')
class AdjusterDelete(DeleteView):
    model = Adjuster
    success_url = reverse_lazy('adjusters')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'dashboard/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse_lazy('map'))
    else:
        return HttpResponseRedirect("{}?invalid".format(reverse_lazy('login'),))
