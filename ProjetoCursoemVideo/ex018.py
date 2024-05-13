# Faça um programa que leia um ângulo qualquer e,
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
a = float(input("Diga o valor de um ângulo "))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('-'*30)
print("O valor de seno é:{0:.2f}!".format(s))
print("O valor do cesseno é: {0:.2}!".format(c))
print("O valor da tangente é: {0:.2f}!".format(t))
