from django.db import models
from apps.accounts.models import Accounts


class Operations(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    operationStatus = models.CharField(max_length=64)
    operationAmount = models.FloatField()
    operationId = models.CharField(max_length=36, unique=True)

    def __str__(self) -> str:
        return f'{self.account} -> {self.operationAmount}'
