# Faça um programa que leia um número qualquer e mostre o seu fatorial.

"""n = int(input("Diga um número para saber o seu fatorial: "))
resultado = 1
cont = 1

while n != cont:
    cont += 1
    resultado *= cont
    print(resultado, end=' --> ')

print("O resultado do fatorial de {} é: {}".format(n, resultado))"""

from math import factorial
numero = int(input("Digite um número para saber o seu fatorial: "))
cont = numero
while cont > 0:
    print("{}".format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    cont -= 1
print(factorial(numero))
