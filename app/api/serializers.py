from rest_framework import serializers
from .models import Stock
from .models import Price
from .models import Predict

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        model = Price
        model = Predict
