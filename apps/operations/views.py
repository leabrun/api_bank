from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Operations
from .serializers import OperationsSerializer
from apps.accounts.models import Accounts


class OperationsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, accountId):
        account = Accounts.objects.get(accountId=accountId).pk
        operations = Operations.objects.filter(account=account)
        serializer = OperationsSerializer(operations, many=True)
            
        return Response(serializer.data, status=status.HTTP_200_OK)
