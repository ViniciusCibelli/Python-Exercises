#Escreva um programa que faça o computador “pensar”
#em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
numeroa = random.randrange(6) #ou random.randint(0, 5)
print("Estou pensando em um número....")
time.sleep(1)
print("Tente adivinhar!")
time.sleep(1)
numeroe = int(input("Escolha um número entre 0 e 5: "))
time.sleep(1)
print("Hmmmmm...")
time.sleep(2)
if numeroe == numeroa:
    print("PARABÉNS, VOCÊ VENCEU!")
else:
    print("Que pena! Você errou! Tente novamente!")
print("----FIM----")
