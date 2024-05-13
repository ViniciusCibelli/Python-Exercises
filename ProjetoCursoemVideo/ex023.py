"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
digitos separados. Ex: 1894
unidade: 4
dezena: 9
centena: 8
milhar: 1
"""

numero = input("Digite um n: ")
numero = "0"*(4-len(numero))+numero
print("Unidade: {} \nDezena:{} \nCentena: {} \nMilhar:{}".format(numero[3], numero[2], numero[1], numero[0]))
