# jeju_app/serializers.py

from rest_framework import serializers
from .models import JejuTouristSpot

class JejuTouristSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = JejuTouristSpot
        fields = '__all__'  # 모든 필드 포함

