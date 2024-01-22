from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Companies
from .serializers import CompaniesSerializer


class CompaniesAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        companies = Companies.objects.filter(owner=request.user)
        serializer = CompaniesSerializer(companies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
