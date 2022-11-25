from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import APIView

router = DefaultRouter()
router.register('data', APIView)

urlpatterns = [
    path('', include(router.urls)),
]
