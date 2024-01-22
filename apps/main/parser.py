"""A module for parsing data from ModuleBank"""

import requests
import json


ROOT_API = 'https://api.modulbank.ru/v1/'


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
