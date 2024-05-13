# Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

import emoji
from time import sleep
print("FALTAM 10 SEGUNDOS PARA A VIRADA DE ANO!!!")
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(":fireworks: :fireworks: :fireworks: :fireworks:", use_aliases=True))
print("FELIZ ANO NOVO!!")
print(emoji.emojize(":fireworks: :fireworks: :fireworks: :fireworks:", use_aliases=True))
