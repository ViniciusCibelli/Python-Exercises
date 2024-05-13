# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input("Informe o cateto oposto do triângulo "))
ca = float(input("Informe o cateto adjacente do triângulo "))
h = math.hypot(co,ca)
print("A hipotenusa do triângulo retângulo de lado {0} e {1}, é: {2:.1f}".format(co, ca, h))

"""
from math import hypot
co = float(input("Diga o valor do cateto oposto "))
ca = float(input("Diga o valor do cateto adjacente "))
print('-'*30)
print("A hipotenusa do triangulo é: {0:.2f}".format(hypot(co, ca)))
"""
