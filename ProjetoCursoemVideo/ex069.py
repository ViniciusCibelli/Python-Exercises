# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

idade = ''
sexo = ''
resposta = ''
maiores = 0
contH = 0
contM = 0
while True:
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Qual o seu sexo? [M/F] ")).strip().upper()
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        contH += 1
    elif sexo == 'F' and idade < 20:
        contM += 1
    elif sexo != 'M' and sexo != 'F':
        print("Resposta inválida, tente novamente!")
        sexo = str(input("Qual o seu sexo? [M/F] ")).strip().upper()
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if resposta == 'S':
        print("Certo! Cadastre o novo candidato:")
    elif resposta == 'N':
        break
    elif resposta != 'S' and resposta != 'N':
        print("Resosta inválida, tente novamente!")
        resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
        print("Certo! Cadastre o novo candidato:")

print("Encerrando processo... volte sempre!")
print('-=' * 24)
print(f"Foram cadastrados {maiores} pessoas maior de 18 anos.")
print(f"Foram cadastrados {contH} homens.")
print(f"Foram cadastradas {contM} mulheres menores de 20 anos.")
print('-=' * 24)
print("FIM")