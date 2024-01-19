"""A module for processing operations"""

from .models import Operations


def savingOperation(pk, operation: dict):
    object = Operations.objects.create(account = pk,
                              operationStatus = operation["status"],
                              operationAmount = operation["amount"],
                              operationId = operation["id"])
    
    return object
