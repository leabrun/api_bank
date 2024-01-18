from django.db import models
from apps.companies.models import Companies


class Accounts(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    accountName = models.CharField(max_length=64)
    accountBalance = models.FloatField()
    accountNumber = models.CharField(max_length=20)
    accountId = models.CharField(max_length=36, unique=True)

    def __str__(self) -> str:
        return f'{self.company} -> {self.accountName}'
