from rest_framework import serializers
from .models import PRICES


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRICES
