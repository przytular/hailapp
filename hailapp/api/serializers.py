from rest_framework import serializers
from dashboard.models import Adjuster, Claim


class ClaimSerializer(serializers.ModelSerializer):

	class Meta:
		model = Claim
		fields = '__all__'