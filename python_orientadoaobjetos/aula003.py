"""na hora de construir um objeto o python usa uma função construtora
#__init__(self)
self é a referencia que encontra o objeto que está sendo construido na memoria
self.variavel trabalha com os atributos no objeto
as caracteristicas de uma classe são chamadas de atributos
métodos são as funções do objeto, o que ele faz. Deve ser adicionado dentro da classe
para usar o método use #nome_da_variavel.método()"""


class Account:

    def __init__(self, number, owner, amount, limit=1000.0):
        print(f"Construindo objeto ... {self}")
        self.number = number
        self.owner = owner
        self.amount = amount
        self.limit = limit

    def statement(self):
        print(f"{self.owner} your bank statement have {self.amount} dollars")

    def deposit(self, value):
        self.amount += value
        print(f"You deposited {value} in you bank account, now you have {self.amount} dollars.")

    def withdraw(self, value):
        if self.amount - value < -1000:
            print("You are not able to withdraw that money.")
        else:
            self.amount -= value
            print(f"You withdrew {value} from you bank account, now you have {self.amount} dollars.")
