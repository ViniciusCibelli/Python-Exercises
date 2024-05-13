"""ENCAPSULAR O ACESSO AOS ATRIBUTOS = para tornar o acesso aos atributos do objeto privado:
   $self.__nome-do-atributo --> USAR 2 UNDERLINE
   Para zerar uma variavel usar #nome-da-variavel = none --> também é possivel usar isso em um objeto sem perder-lo"""


class Account:

    def __init__(self, number, owner, amount, limit=1000.0):
        self.__number = number
        self.__owner = owner
        self.__amount = amount
        self.__limit = limit
        print(f"Construindo objeto ... {self}")

    def statement(self):
        print(f"{self.__owner} your bank statement have {self.__amount} dollars")

    def deposit(self, value):
        self.__amount += value
        print(f"It was deposited {value} dollars in you bank account, {self.__owner}.")

    def withdraw(self, value):
        if self.__amount - value < -1000:
            print("You are not able to withdraw that money.")
        else:
            self.__amount -= value
            print(f"You withdrew {value} from you bank account, {self.__owner}.")

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)

    def __str__(self):
        return f"{self.__owner}"

    def __add__(self, other):
        return self.__amount + other.__amount
