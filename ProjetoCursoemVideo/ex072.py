#  Crie um programa que tenha uma tupla totalmente preenchida
#  com uma contagem por extenso, de zero até vinte.
#  Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
for cont in range(0, len(numeros)):
    escolha = int(input("Digite um número entre 0 e 20: "))
    if escolha > 20:
        print("Tentativa inválida, tente novamente!")
    elif escolha < 0:
        print("Tentativa inválida, tente novamente!")
    else:
        print(f"Você escolheu o número \033[34m{numeros[escolha]}\033[m")
        break
