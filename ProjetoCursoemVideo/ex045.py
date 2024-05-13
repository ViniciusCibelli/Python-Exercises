# Crie um programa que faça o computador jogar Jokenpô com você.
"""
from random import choice
from time import sleep
print('[1] - Pedra')
print('[2] - Papel')
print('[3] - Tesoura')
#sleep(1)
escolha = int(input("Escolha uma das opções acima: "))
opcoespc = ['Pedra', 'Papel', 'Tesoura']
escolhapc = choice(opcoespc)
if escolha == 1 and escolhapc == 'Pedra':
    print("O computador lançou pedra e \033[33mEMPATOU\033[m")
elif escolha == 1 and escolhapc == 'Tesoura':
    print("O computador lançou tesoura, você \033[32mGANHOU\033[m")
elif escolha == 1 and escolhapc == 'Papel':
    print("O computador lançou papel e você \033[31mPERDEU\033[m")
elif escolha == 2 and escolhapc == 'Pedra':
    print("O computador lançou pedra, você \033[32mGANHOU\033[m")
elif escolha == 2 and escolhapc == 'Tesoura':
    print("O computador lançou tesoura, você \033[31mPERDEU\033[m")
elif escolha == 2 and escolhapc == 'Papel':
    print("O computador lançou papel e \033[33mEMPATOU\033[m")
elif escolha == 3 and escolhapc == 'Pedra':
    print("O computador lançou pedra e você \033[31mPERDEU\033[m")
elif escolha == 3 and escolhapc == 'Tesoura':
    print("O computador lançou tesoura e \033[33mEMPATOU\033[m")
elif escolha == 3 and escolhapc == 'Papel':
    print("O computador lançou papel e você \033[32mGANHOU\033[m")
else:
    print("Escolha uma opção válida!")
"""

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("Suas opções:")
print("[ 0 ] - PEDRA")
print("[ 1 ] - PAPEL")
print("[ 2 ] - TESOURA")
jogador = int(input("Qual a sua jogada: "))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!!")
sleep(0.5)
print("-=" * 15)
sleep(0.5)
print("O computador escolheu {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
print("-=" * 15)
sleep(0.5)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('VOCÊ PERDEU')
    else:
        print("Jogada Invalida")
if computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print("Jogada Invalida")
if computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print("Jogada Invalida")
