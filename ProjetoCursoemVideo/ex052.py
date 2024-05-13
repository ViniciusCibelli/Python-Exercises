# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um número: "))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        total += 1 # ou total = total + 1
print("O número {} foi dividido {} vezes".format(n, total))
if total == 2:
    print("É primo!")
else:
    print("Não é primo!")
