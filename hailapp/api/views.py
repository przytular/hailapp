# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ClaimSerializer

from dashboard.models import Claim
from rest_framework.generics import ListAPIView, UpdateAPIView


class LocationUpdate(APIView):

	def post(self,  request, format=None):
		latitude = request.POST.get('latitude', None)
		longitude = request.POST.get('longitude', None)
		adjuster = request.user.adjuster
		if latitude and longitude:
			adjuster.lng = longitude
			adjuster.lat = latitude
			adjuster.save()
			return Response("OK")
		else:
			return Response({"details": "You must specify latitude and logitude."}, status=403)


class ClaimsAPI(ListAPIView):
	queryset = Claim.objects.all()
	serializer_class = ClaimSerializer


class PushIDUpdateAPI(APIView):
	def post(self, request, format=None):
		push_id = request.POST.get('push_id', None)
		if push_id:
			request.user.adjuster.push_id = push_id
			request.user.save()
			return Response("OK")
		else:
			return Response({"details": "No push_id specified"})


class UpdateClaimAPIView(UpdateAPIView):
	queryset = Claim
	serializer_class = ClaimSerializer