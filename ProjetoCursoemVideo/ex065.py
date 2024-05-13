# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = 0
maior = 0
menor = 0
soma = 0
cont = 0
resposta = 'S'
while resposta == 'S':
    numero = int(input("Digite um número: "))
    soma += numero
    cont += 1
    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if resposta != 'S' and resposta != 'N':
        print("Resposta inválida, tente novamente!")
    if numero > maior:
        maior = numero
    else:
        menor = numero
print("O \033[32mmaior\033[m número digitado foi: {}".format(maior))
print("O \033[31mmenor\033[m número digitado foi: {}".format(menor))
print("A \033[33msoma\033[m dos números \033[35m{}\033[m foi: {}".format(cont, soma))
print("A \033[34mmédia\033[m dos números digitados é: {:.1f}".format(soma / cont))
