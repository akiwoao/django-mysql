from rest_framework import viewsets
from .models import Price
from .serializers import APISerializer


class APIView(viewsets.ModelViewSet):

    queryset = Price.objects.all()
    serializer_class = APISerializer
