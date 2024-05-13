# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n1 > n2 and n3 > n2:
    menor = n2
if n1 > n3 and n2 > n3:
    menor = n3
print("O maior valor é: {} \nE o menor valor é: {}".format(maior, menor))
