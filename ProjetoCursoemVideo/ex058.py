# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer

import random
from time import sleep
computador = random.randint(1, 10)
cont = 0
escolha = ''
print("Eu sou seu computador...")
sleep(0.5)
print("Vamos jogar um jogo de advinhação, eu vou pensar em um número de 0 a 10! Tente adivinhar!")
sleep(1.5)
while escolha != computador:
    escolha = int(input("Escolha um número entre 1 e 10: "))
    if escolha == computador:
        print("\033[32mParábens, você ganhou!!\033[m")
        cont += 1
    elif escolha > 10 or escolha < 1:
        print("\033[33mTentariva invalida, tente novamente!!\033[m")
    else:
        print("\033[31mQue pena você errou!!\033[m")
        if escolha > computador:
            print("Tente um número \033[35mmenor\033[m.")
        else:
            print("Tente um número \033[36mmaior\033[m.")
        cont += 1
print("Você precisou de \033[34m{} tentativa(s)\033[m para acertar!".format(cont))
