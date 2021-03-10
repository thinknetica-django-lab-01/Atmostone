from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apps.main.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
