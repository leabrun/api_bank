"""A module for processing companies"""

from .models import Companies


def savingCompany(user, company: dict):
    object = Companies.objects.create(owner=user,
                             companyName=company["companyName"],
                             companyId=company["companyId"],)
    
    return object
