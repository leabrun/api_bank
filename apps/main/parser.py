"""A module for parsing data from ModuleBank"""

import requests
import json
from apps.companies.tools import savingCompany
from apps.accounts.tools import savingAccount
from apps.operations.tools import savingOperation


ROOT_API = 'https://api.modulbank.ru/v1/'
TOKEN = 'YzgzZjU2ZDMtMzliZS00ZmZjLWI0NmMtYzYxNDU3YzFjZThkY2NmOWZjZjYtNjMwNC00NzQ3LThmMWQtMjQ3ZTU3YjI0M2I5'


def get_json(data: str) -> list:
    return json.loads(data)


def get_headers(token: str) -> dict:
    return {'Authorization': "Bearer {}".format(token)}


def get_account_info(headers: dict) -> list:
    full_url = ROOT_API + 'account-info'
    data = requests.post(full_url, headers=headers).text

    return get_json(data)

def get_operation_history(id: str, headers: dict) -> list:
    full_url = ROOT_API + f'operation-history/{id}'
    data = requests.post(full_url, headers=headers).text

    return get_json(data)


def connect_token(user, token: str):
    headers = get_headers(token)
    account_info = get_account_info(headers)

    for company in account_info:
        objectCompany = savingCompany(user, company)
        for account in company["bankAccounts"]:
            objectAccount = savingAccount(objectCompany, account)
            operation_history = get_operation_history(account["id"], headers)

            for operation in operation_history:
                savingOperation(objectAccount, operation)
