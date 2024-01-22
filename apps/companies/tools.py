"""A module for processing companies"""

from django.contrib.auth.models import User
from .models import Companies


def savingCompany(user: int, company: dict):
    owner = User.objects.get(id=user)
    object = Companies.objects.create(owner=owner,
                             companyName=company["companyName"],
                             companyId=company["companyId"],)
    
    return object
