from rest_framework import viewsets
from .models import PRICES
from .serializers import PriceSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = PRICES.objects.all()
    serializer_class = PriceSerializer
