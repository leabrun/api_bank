from rest_framework import serializers
from .models import Operations


class OperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operations
        fields = ('account',  'operationStatus', 'operationAmount',  'operationId')
