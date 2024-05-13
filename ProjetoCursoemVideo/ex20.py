# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
aluno1 = str(input("Digite o nome do primeiro aluno: "))
aluno2 = str(input("Digite o nome do segundo aluno: "))
aluno3 = str(input("Digite o nome do terceiro aluno: "))
aluno4 = str(input("Digite o nome do quarto aluno: "))
sorteio = aluno1, aluno2, aluno3, aluno4
print('-'*30)
print("Dentre os alunos sorteados, a ordem dos alunos é: \n{}!".format(random.sample([aluno1, aluno2, aluno3, aluno4], k=4)))

"""
import random
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("Dentre os alunos sorteados, a ordem de apresentação dos alunos é:")
print(lista)
"""


