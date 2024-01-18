from rest_framework import generics
from .models import Accounts
from .serializers import AccountsSerializer


class AccountsAPIView(generics.ListAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
