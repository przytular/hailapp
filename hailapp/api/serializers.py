from rest_framework import serializers
from dashboard.models import Adjuster, Claim, ClaimField


class ClaimFieldSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClaimField
		fields = '__all__'


class ClaimSerializer(serializers.ModelSerializer):
	class Meta:
		model = Claim
		exclude = ['adjusters']


class ClaimFieldPhotoSerializer(serializers.Serializer):
    image = serializers.ImageField()
