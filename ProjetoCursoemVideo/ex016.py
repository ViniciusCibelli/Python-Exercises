# Crie um programa que leia um número Real qualquer pelo teclado e,
# mostre na tela a sua porção inteira

from math import trunc
n = float(input("Informe um número qualquer: "))
# pi = trunc(n)
print('='*30)
print("A posição inteira de \033[31m{0}\033[m é: \033[32m{1}\033[m!".format(n, trunc(n)))

"""
import math
n = float(input("Informe um número qualquer "))
pi = math.trunc(n)
print('='*30)
print("O número digitado foi {0} e sua porção inteira é {1}!".format(n, pi))
"""