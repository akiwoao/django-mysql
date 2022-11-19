from rest_framework import viewsets
from .models import TestOHLC
from .serializers import APISerializer


class APIView(viewsets.ModelViewSet):

    queryset = TestOHLC.objects.all()
    serializer_class = APISerializer
