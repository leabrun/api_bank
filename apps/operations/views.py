from rest_framework import generics
from .models import Operations
from .serializers import OperationsSerializer


class OperationsAPIView(generics.ListAPIView):
    queryset = Operations.objects.all()
    serializer_class = OperationsSerializer
