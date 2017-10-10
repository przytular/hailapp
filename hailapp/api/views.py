# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ClaimSerializer, ClaimFieldSerializer

from dashboard.models import Claim, ClaimField
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


class UpdateClaimAPIView(APIView):

	def post(self, request, pk, format=None):
		claim = get_object_or_404(Claim, pk=pk)
		post = request.data
		s = ClaimSerializer(data=post)
		if s.is_valid():
			s.save()
		fields = post.get('fields', [])
		for field in fields:
			quarter, section, township, \
			range, meridian = [x.strip() for x in field["location"].split("-")]

			ClaimField.objects.create(claim=claim,
									  type=field['type'],
									  name=field['name'],
									  acres=field['acres'],
									  quarter=quarter,
									  section=section,
									  township=township,
									  range=range,
									  meridian=meridian,
									  loss=field['loss'])
		return Response("OK")

class ClaimFieldsAPI(APIView):

	def get(self, request, pk, format=None):
		fields = ClaimField.objects.filter(claim=get_object_or_404(Claim, pk=pk))
		return Response(ClaimFieldSerializer(fields, many=True).data)

	def post(self, request, pk, format=None):
		claim=get_object_or_404(Claim, pk=pk)

		fields = request.data
		for field in fields:
			quarter, section, township, \
			range, meridian = [x.strip() for x in field["location"].split("-")]

			ClaimField.objects.create(claim=claim,
									  type=field['type'],
									  name=field['name'],
									  acres=field['acres'],
									  quarter=quarter,
									  section=section,
									  township=township,
									  range=range,
									  meridian=meridian,
									  loss=field['loss'])
		return Response("OK")
