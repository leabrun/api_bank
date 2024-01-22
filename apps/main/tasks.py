from celery import shared_task
from django.db import transaction
from .parser import get_headers, get_account_info, get_operation_history
from apps.companies.tools import savingCompany
from apps.accounts.tools import savingAccount
from apps.operations.tools import savingOperation


@shared_task
def connect_token_async(user: int, token: str) -> bool:
    headers = get_headers(token)
    account_info = get_account_info(headers)

    with transaction.atomic():
        for company in account_info:
            objectCompany = savingCompany(user, company)
            for account in company["bankAccounts"]:
                objectAccount = savingAccount(objectCompany, account)
                operation_history = get_operation_history(account["id"], headers)

                for operation in operation_history:
                    savingOperation(objectAccount, operation)

    return True
