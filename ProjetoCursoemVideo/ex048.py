# Faça um programa que calcule a soma entre todos os números que
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

from time import sleep
s = 0
cont = 0
print("De todos os números entre 1 e 500...")
sleep (1)
for c in range(1, 501):
    if (c % 3) == 0:
        cont = cont + 1
        s = s + c
print("A soma de todos os {} valores solicitados, no intervalo de 1 até 500 é: {}".format(cont, s))
