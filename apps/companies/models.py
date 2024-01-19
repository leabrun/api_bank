from django.db import models
from django.contrib.auth.models import User


class Companies(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=64)
    companyId = models.CharField(max_length=36, unique=True)

    def __str__(self) -> str:
        return self.companyName