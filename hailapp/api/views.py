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
			request.user.adjuster.save()
			return Response("OK")
		else:
			return Response({"details": "No push_id specified"})


class UpdateClaimAPIView(UpdateAPIView):
	serializer_class = ClaimSerializer
	queryset = Claim.objects.all()


class ClaimFieldsAPI(APIView):

	def get(self, request, pk, format=None):
		fields = ClaimField.objects.filter(claim=get_object_or_404(Claim, pk=pk))
		return Response(ClaimFieldSerializer(fields, many=True).data)

	def post(self, request, pk, format=None):
		field_id = request.data.get('field_id', None)
		if field_id:
			claim_field = get_object_or_404(ClaimField, pk=field_id)
			s = ClaimFieldSerializer(claim_field, data=request.data, partial=True)
			if s.is_valid():
				s.save()
				return Response(s.data)
			else:
				return Response(s.errors)

		else:
			claim=get_object_or_404(Claim, pk=pk)
			fields = request.data
			old_fields = ClaimField.objects.filter(claim=claim)
			for field in fields:
				try:
					quarter, section, township, \
					range, meridian = [x.strip() for x in field["location"].split("-")]
				except TypeError:
					quarter, section, township, range, meridian = ('',)*5

				ClaimField.objects.create(claim=claim,
										  type=field['type'],
										  name=field['name'],
										  acres=field['acres'],
										  quarter=quarter,
										  section=section,
										  township=township,
										  range=range,
										  meridian=meridian,
										  loss=field['loss'],
										  completed=field['completed'])
			old_fields.delete()
			return Response(ClaimFieldSerializer(fields, many=True).data)
