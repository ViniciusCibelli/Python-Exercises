# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.

print("Caso deseje parar de inserir números: Digite [999]")
cont = 0
numero = 0
soma = 0
while numero != 999:
    numero = int(input("Digite um número: "))
    soma += numero
    if numero == 999:
        soma -= numero
    else:
        cont += 1
print("Você digitou \033[32m{}\033[m números!".format(cont))
print("A soma dos números digitados é: \033[33m{}\033[m".format(soma))
print("FIM")
