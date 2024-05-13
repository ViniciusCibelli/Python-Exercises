# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato

total = mil = barato = preco = 0
resposta = ''
produto = ''
while True:
    produto = str(input("Digite o nome do produto: ")).capitalize()
    preco = float(input("Digite o valor desse produto  R$"))
    total += preco

    if preco >= 1000:
        mil += 1

    if barato > preco or barato == 0:
        barato = preco
        nome = produto

    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print("Resosta inválida, tente novamente!")
        resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if resposta == 'S':
        print("\033[34mCerto, cadastre um novo produto:\033[m")
    elif resposta == 'N':
        break

print(f"O total gasto foi R${total}.")
print(f"De todos os produtos, {mil} custaram mais do que mil reais.")
print(f"O produto mais barato foi: {nome}")
