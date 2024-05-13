"""METODOS ESTÁTICOS podem ser chamados sem a referencia, fazem parte da classe #@staticmethod --> não precisam do self
   faz sentido usar métodos estaticos quando todos objetos possuirem algo em comum.
    """


class Account:

    def __init__(self, number, owner, amount, limit):
        self.__number = number
        self.__owner = owner
        self.__amount = amount
        self.__limit = limit
        print(f"Building object ... {self}")

    def statement(self):
        print(f"{self.__owner} your bank statement have {self.__amount} dollars")

    def deposit(self, value):
        self.__amount += value
        print(f"It was deposited {value} dollars in you bank account, {self.__owner}.")

    def __withdraw_possible(self, value):
        return value <= self.__amount + self.__limit

    def withdraw(self, value):
        if self.__withdraw_possible(value):
            print(f"You withdrew {value} from you bank account, {self.__owner}.")
            self.__amount -= value
        else:
            print("You are not able to withdraw that money.")

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)

    def __str__(self):
        return f"{self.__owner}"

    @property
    def amount(self):
        return self.__amount

    @property
    def owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value
        print(f"O limite da conta foi alterado para {value}")

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def bank_codes():
        return {"ITAU": "007", "CAIXA": "123", "BRADESCO": "321", "SANTANDER": "666"}


class Client:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name.title()

    @name.setter
    def name(self, name):
        self.__name = name
