"""Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome."""

nome = input("Digite o seu nome completo: ").strip()
pnome = nome.split()
print("Em maiúsculo fica: {}!".format(nome.upper()))
print("Em minusculo fica: {}!".format(nome.lower()))
#print("A soma das letras do nome completo é: {}!".format(len("".join(pnome))))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print("O primeiro nome tem {} letras!".format(len(pnome[0])))
#print("O seu primeiro nome tem {} letras!" .format(nome.find(' ')))
