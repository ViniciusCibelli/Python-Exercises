"""abir no terminal, #nome da conta = create_acount(number, owner, amount, limit)
    usar essa mesma ideia para todos os comandos abaixo... entretando, ao longo do tempo
    fica muito complicado e deixa de ser organizado. AINDA NÃO HÁ ORIENTAÇÃO A OBJETO!"""


def create_account(number, owner, amount, limit):
    account = {"numero": number, "titular": owner, "saldo": amount, "limite": limit}
    return account


def deposit(account, value):
    account["saldo"] += value


def withdraw(account, value):
    account["saldo"] -= value


def statement(account):
    print("The bank statement is {}".format(account["saldo"]))
