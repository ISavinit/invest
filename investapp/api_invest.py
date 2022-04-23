from tinkoff.invest import Client
from flask import current_app

import json


def get_accounts():
    with Client(current_app.config["TINKOFF_API_TOKEN"]) as client:
        accounts = client.users.get_accounts()
        print("\nСписок текущих аккаунтов\n")
        print(accounts)



