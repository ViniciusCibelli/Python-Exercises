# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

from time import sleep
homem = 0
mulheres = 0
maior_idade = 0
soma = 0
for pessoas in range(1, 5):
    print("{} {}ª PESSOA {}".format('-' * 7, pessoas, '-' * 7))
    nome = str(input("Digite um nome: ")).capitalize().strip()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Sexo [H/M]: ")).upper().strip()
    soma += idade

    if sexo == 'H' and idade > maior_idade:
        maior_idade = idade
        homem = nome

    if sexo == 'M' and idade < 20:
        mulheres += 1

print("A \033[34mmédia das idades é: {:.1f}\033[m!".format(soma / 4))
sleep(1)
print("O \033[31mhomem mais velho\033[m tem \033[32m{} anos\033[m e se chama \033[33m{}\033[m!".format(maior_idade, homem))
sleep (1)
print("Há \033[35m{} mulher(es) menor(es) de 20 anos\033[m de idade!".format(mulheres))
