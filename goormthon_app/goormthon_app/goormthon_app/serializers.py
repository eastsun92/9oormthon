# jeju_app/serializers.py

from rest_framework import serializers
from .models import JejuTouristSpot

class JejuTouristSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = JejuTouristSpot
        fields = ('name', 'lat', 'lon', 'url', 'phone_number', 'address')

