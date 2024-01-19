from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Accounts
from .serializers import AccountsSerializer
from apps.companies.models import Companies

class AccountsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, companyId):
        company = Companies.objects.get(companyId=companyId).pk
        accounts = Accounts.objects.filter(company=company)
        serializer = AccountsSerializer(accounts, many=True)
            
        return Response(serializer.data, status=status.HTTP_200_OK)
