"""ABC - Abstract Base Classes
biblioteca de classes abstratas para serem herdadas - complementa duck typing
"""

from abc import ABC

from collections.abc import Sized


class Mylist(Sized):
    def __init__(self, descrition):
        self.descrition = descrition

    def __str__(self):
        return self.descrition

list = Mylist()
print(list)

# o erro aqui é proposital, a classe só irá funcionar caso seja implementado todos os metodos citados no erro.