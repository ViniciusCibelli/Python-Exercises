# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

s = 0
cont = 0
for c in range(1, 7):
    numeros = int(input("Digite o {}° número: ".format(c)))
    if numeros % 2 == 0:
        s += numeros
        cont += 1
print("Você informou {} numeros pares e a soma deles pares é igual a: {}".format(cont,s))
print("Os outros valores digitados eram impares e foram desconsiderados")
