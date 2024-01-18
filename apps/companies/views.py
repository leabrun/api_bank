from rest_framework import generics
from .models import Companies
from .serializers import CompaniesSerializer


class CompaniesAPIView(generics.ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
