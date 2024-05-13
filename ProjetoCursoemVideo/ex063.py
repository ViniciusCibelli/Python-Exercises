# Escreva um programa que leia um número N inteiro qualquer
# E mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print("{} SEQUÊNCIA DE FIBONACCI {}".format('-=' * 5, '-=' * 5))
print('-=-' * 15)
n = int(input("Quantos números da sequência você quer saber? "))
termo1 = 0
termo2 = 1
print("O {:2}° termo é: {}".format(1, termo1))
print("O {:2}° termo é: {}".format(2, termo2))
cont = 3
while cont <= n:
    termo3 = termo1 + termo2
    print("O {:2}° termo é: {}".format(cont, termo3))
    termo1 = termo2
    termo2 = termo3
    cont += 1
print("FIM")
print('-=-' * 15)
