from rest_framework import viewsets
from .serializers import *
from .models import *

class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
