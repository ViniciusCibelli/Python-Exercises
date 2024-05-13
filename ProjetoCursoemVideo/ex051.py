# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input("Digite qual o primeiro valor da sua PA: "))
razao = int(input("Digite qual a razão da sua PA: "))
for c in range(1, 11):
    an = a1 + (c - 1) * razao
    print("O {:2}° termo da sua PA é: {}".format(c, an))