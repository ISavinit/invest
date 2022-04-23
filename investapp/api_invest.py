from tinkoff.invest import Client
from flask import current_app
from investapp.portal.models import Account
from investapp.db import db

import json


def get_accounts():
    with Client(current_app.config["TINKOFF_API_TOKEN"]) as client:
        accounts = client.users.get_accounts()
        print("\nСписок текущих аккаунтов\n")
        for account in accounts.accounts:
            print(account)
            print('id = ', account.id)
            print('type = ', type(account.type))
            print('name = ', account.name)
            print('status = ', account.status)
            print('open = ', account.opened_date)
            print('close =', account.closed_date)


def save_accs(ac_id, ac_type, ac_name, ac_status, ac_open, ac_close):
    accs = Account(ac_id=ac_id, ac_type=ac_type, ac_name=ac_name,
                      ac_status=ac_status, ac_open=ac_open, ac_close=ac_close)
    db.session.add(accs)

def del_accs():
    db.session.query(Account).delete()
    db.session.commit()
