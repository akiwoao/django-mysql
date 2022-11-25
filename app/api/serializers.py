from rest_framework import serializers
from .models import *


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('date', 'open', 'high', 'low', 'close')


class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predict
        fields = ('date', 'predict', 'up_down', 'propriety')


class StockSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True, read_only=True)
    predicts = PredictSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = ('id', 'name', 'country', 'prices', 'predicts')
