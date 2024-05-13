# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário,
# 2 para octal e
# 3 para hexadecimal.

numero = int(input("Digite um número inteiro: "))
print("[1] - Binário \n[2] - Octal \n[3] - Hexadecimal")
resposta = int(input("Digite [1], [2] ou [3]: "))
if resposta == 1:
    numeroconvertido = format(numero, "b")
elif resposta == 2:
    numeroconvertido = format(numero, "o")
elif resposta == 3:
    numeroconvertido = format(numero, "x")
print("O número \033[31m{}\033[m convertido  é: \033[33m{}\033[m!".format(numero, numeroconvertido))
