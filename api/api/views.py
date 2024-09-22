from rest_framework import viewsets
from .models import Test
from .serializers import TestModelSerializer

class TestModelViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestModelSerializer
