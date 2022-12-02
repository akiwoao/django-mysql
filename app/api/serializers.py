from rest_framework import serializers
from .models import *
from datetime import date
from dateutil.relativedelta import relativedelta


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('date', 'open', 'high', 'low', 'close')


class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predict
        fields = ('date', 'predict', 'up_down', 'propriety')


class StockSerializer(serializers.ModelSerializer):
    prices = serializers.SerializerMethodField()
    predicts = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = ('id', 'name', 'country', 'prices', 'predicts')

    def get_prices(self, obj):
        # 本番ではtodayに変更
        end = date(2021, 12, 31)
        start = end - relativedelta(months=3)
        price_query = Price.objects.filter(date__range=(f'{start}', f'{end}'))
        serializer = PriceSerializer(price_query, many=True)
        return serializer.data

    def get_predicts(self, obj):
        # 本番ではtodayに変更
        end = date(2021, 12, 31)
        start = end - relativedelta(months=3)
        predict_query = Predict.objects.filter(date__range=(f'{start}', f'{end}'))
        serializer = PredictSerializer(predict_query, many=True)
        return serializer.data
