# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
pessoas = 0
a = date.today().year
print(a)
for c in range(1, 8):
    ano = int(input("Digite o ano do seu nascimento: "))
    if (a - ano) > 18:
        print("Você têm {} anos e já é \033[33mmaior de idade\033[m!".format(a - ano))
        pessoas += 1
    else:
        print("Você têm {} anos e ainda é \033[31mmenor de idade\033[m!".format(a - ano))
print("Das 7 pessoas acima, {} são maiores de idade e {} ainda são menores!".format(pessoas, 7 - pessoas))