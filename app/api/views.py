from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer


class APIView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
