"""A module for processing accounts"""

from .models import Accounts


def savingAccount(pk, account: dict):
    object = Accounts.objects.create(company = pk,
                            accountName = account["accountName"],
                            accountBalance = account["balance"],
                            accountNumber = account["number"],
                            accountId = account["id"])
    
    return object
