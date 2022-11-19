from rest_framework import serializers
from .models import TestOHLC


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = TestOHLC
